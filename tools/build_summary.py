from __future__ import annotations

import html
import os
import sys
import time
from collections import Counter
from datetime import date
from pathlib import Path, PurePosixPath
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
ROUNDS = ROOT / "rounds"
SUMMARY = ROOT / "SUMMARY.md"
LOCK = ROOT / ".summary.lock"

ALLOWED_STATUSES = (
    "pending",
    "working",
    "candidate",
    "blocked",
    "accepted",
    "rejected",
)
ALLOWED_CONFIDENCE = ("", "low", "medium", "high")
ALLOWED_KINDS = ("puzzle", "subpuzzle", "meta")
ALLOWED_ROUND_FEEDER = ("yes", "no")
LOCK_TIMEOUT_SECONDS = 30.0
STALE_LOCK_SECONDS = 120.0


def acquire_lock() -> None:
    deadline = time.monotonic() + LOCK_TIMEOUT_SECONDS
    while True:
        try:
            descriptor = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                stream.write(f"{os.getpid()}\n")
            return
        except FileExistsError:
            try:
                age = time.time() - LOCK.stat().st_mtime
                if age > STALE_LOCK_SECONDS:
                    LOCK.unlink()
                    continue
            except FileNotFoundError:
                continue

            if time.monotonic() >= deadline:
                raise TimeoutError(f"Timed out waiting for {LOCK}")
            time.sleep(0.1)


def release_lock() -> None:
    try:
        LOCK.unlink()
    except FileNotFoundError:
        pass


def read_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening frontmatter delimiter")

    result: dict[str, str] = {}
    closing_index: int | None = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break
        key, separator, value = line.partition(":")
        if separator:
            result[key.strip().lower()] = value.strip().strip("\"'")

    if closing_index is None:
        raise ValueError("missing closing frontmatter delimiter")
    body = "\n".join(lines[closing_index + 1:])
    return result, body


def read_round(round_dir: Path) -> tuple[str, list[str]]:
    errors: list[str] = []
    round_file = round_dir / "ROUND.md"
    if not round_file.exists():
        return round_dir.name, [f"{round_dir.name}: missing ROUND.md"]

    try:
        data, _ = read_frontmatter(round_file)
    except (OSError, UnicodeError, ValueError) as error:
        return round_dir.name, [f"{round_dir.name}/ROUND.md: {error}"]

    round_id = data.get("round_id", "")
    title = data.get("title", "")
    if round_id != round_dir.name:
        errors.append(
            f"{round_dir.name}/ROUND.md: round_id must match its directory name"
        )
    if not title:
        errors.append(f"{round_dir.name}/ROUND.md: title is required")
    return title or round_dir.name, errors


def parse_feeders(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def feeder_pool_round(feeder: str, current_round: str) -> str | None:
    if feeder == "all-round-feeders":
        return current_round
    suffix = "/all-round-feeders"
    if feeder.endswith(suffix):
        return feeder[: -len(suffix)] or None
    return None


def safe_shared_source(value: str) -> bool:
    if not value:
        return True
    path = PurePosixPath(value.replace("\\", "/"))
    return not path.is_absolute() and ".." not in path.parts


def validate_record(
    label: str,
    expected_round: str,
    data: dict[str, str],
    body: str,
) -> list[str]:
    errors: list[str] = []
    status = data.get("status", "")
    confidence = data.get("confidence", "")
    answer = data.get("answer", "")
    summary = data.get("summary", "")
    updated = data.get("updated", "")
    kind = data.get("kind", "")
    round_id = data.get("round", "")
    parent = data.get("parent", "")
    source = data.get("source", "")
    round_feeder = data.get("round_feeder", "")
    feeders = data.get("feeders", "")

    if kind not in ALLOWED_KINDS:
        errors.append(
            f"kind must be one of {', '.join(ALLOWED_KINDS)}; got {kind!r}"
        )
    if round_id != expected_round:
        errors.append(
            f"round must match directory {expected_round!r}; got {round_id!r}"
        )
    if kind == "subpuzzle" and not parent:
        errors.append("subpuzzle requires parent")
    if kind == "meta" and not feeders:
        errors.append("meta requires explicit feeders or unknown")
    if round_feeder not in ALLOWED_ROUND_FEEDER:
        errors.append("round_feeder must be yes or no")
    if "unknown" in parse_feeders(feeders) and feeders.strip() != "unknown":
        errors.append("feeders: unknown may not be combined with explicit IDs")
    if not safe_shared_source(source):
        errors.append(
            "source must be a safe relative path under Round shared/")

    if status not in ALLOWED_STATUSES:
        errors.append(
            f"status must be one of {', '.join(ALLOWED_STATUSES)}; got {status!r}"
        )
    if confidence not in ALLOWED_CONFIDENCE:
        errors.append(
            "confidence must be blank, low, medium, or high; "
            f"got {confidence!r}"
        )
    if status in {"candidate", "accepted"}:
        if not answer:
            errors.append(f"{status} requires a non-empty answer")
        if not confidence:
            errors.append(f"{status} requires confidence")
    if status == "rejected" and answer:
        errors.append("rejected status requires clearing the current answer")
    if status != "pending":
        if not summary:
            errors.append(f"{status} requires a one-line summary")
        if not updated:
            errors.append(f"{status} requires an updated date")
    if updated:
        try:
            date.fromisoformat(updated)
        except ValueError:
            errors.append("updated must use YYYY-MM-DD")
    if status in {"working", "blocked", "rejected"}:
        heading = "## Next action"
        if heading not in body or not body.split(heading, 1)[1].strip():
            errors.append(f"{status} requires a non-empty Next action section")
    if not data.get("node_id", ""):
        errors.append("node_id is required")
    if not data.get("title", ""):
        errors.append("title is required")

    return [f"{label}: {message}" for message in errors]


def collect_records() -> tuple[
    list[dict[str, str]],
    dict[str, str],
    list[str],
    list[str],
]:
    records: list[dict[str, str]] = []
    round_titles: dict[str, str] = {}
    errors: list[str] = []
    warnings: list[str] = []
    seen_keys: set[str] = set()

    if not ROUNDS.exists():
        return records, round_titles, errors, warnings

    for round_dir in sorted(ROUNDS.iterdir(), key=lambda item: item.name.lower()):
        if not round_dir.is_dir() or round_dir.name.startswith("_"):
            continue

        round_title, round_errors = read_round(round_dir)
        round_titles[round_dir.name] = round_title
        errors.extend(round_errors)

        nodes = round_dir / "nodes"
        if not nodes.exists():
            continue

        for node_dir in sorted(nodes.iterdir(), key=lambda item: item.name.lower()):
            if not node_dir.is_dir() or node_dir.name.startswith("_"):
                continue

            solution = node_dir / "solution.md"
            if not solution.exists():
                records.append(
                    {
                        "round": round_dir.name,
                        "round_title": round_title,
                        "directory": node_dir.name,
                        "node_id": node_dir.name,
                        "title": node_dir.name,
                        "kind": "puzzle",
                        "parent": "",
                        "source": "",
                        "round_feeder": "yes",
                        "feeders": "",
                        "status": "pending",
                        "answer": "",
                        "confidence": "",
                        "summary": "",
                        "updated": "",
                        "has_solution": "",
                    }
                )
                continue

            try:
                data, body = read_frontmatter(solution)
            except (OSError, UnicodeError, ValueError) as error:
                errors.append(f"{round_dir.name}/{node_dir.name}: {error}")
                continue

            label = f"{round_dir.name}/{node_dir.name}"
            errors.extend(
                validate_record(label, round_dir.name, data, body)
            )
            node_id = data.get("node_id", node_dir.name)
            key = f"{round_dir.name}/{node_id}"
            if key in seen_keys:
                errors.append(f"{label}: duplicate key {key!r}")
            seen_keys.add(key)

            records.append(
                {
                    "round": round_dir.name,
                    "round_title": round_title,
                    "directory": node_dir.name,
                    "node_id": node_id,
                    "title": data.get("title", node_dir.name),
                    "kind": data.get("kind", ""),
                    "parent": data.get("parent", ""),
                    "source": data.get("source", ""),
                    "round_feeder": data.get("round_feeder", ""),
                    "feeders": data.get("feeders", ""),
                    "status": data.get("status", ""),
                    "answer": data.get("answer", ""),
                    "confidence": data.get("confidence", ""),
                    "summary": data.get("summary", ""),
                    "updated": data.get("updated", ""),
                    "has_solution": "yes",
                }
            )

    record_keys = {
        f"{record['round']}/{record['node_id']}": record
        for record in records
    }
    for record in records:
        label = f"{record['round']}/{record['node_id']}"
        source = record["source"]
        if source:
            source_path = (
                ROUNDS
                / record["round"]
                / "shared"
                / Path(source.replace("/", os.sep))
            )
            if not source_path.exists():
                warnings.append(
                    f"{label}: shared source {source!r} has not been created"
                )

        feeders = parse_feeders(record["feeders"])
        if feeders == ["unknown"] or not feeders:
            continue

        seen_feeders: set[str] = set()
        for feeder in feeders:
            pool_round = feeder_pool_round(feeder, record["round"])
            if pool_round is not None:
                if pool_round not in round_titles:
                    warnings.append(
                        f"{label}: feeder pool {feeder!r} refers to "
                        "an unknown Round"
                    )
                    continue
                keys = sorted(
                    key
                    for key, candidate in record_keys.items()
                    if candidate["round"] == pool_round
                    and candidate["round_feeder"] == "yes"
                    and key != label
                )
                if not keys:
                    warnings.append(
                        f"{label}: feeder pool {feeder!r} resolves to no Nodes"
                    )
                    continue
            else:
                keys = [
                    feeder
                    if "/" in feeder
                    else f"{record['round']}/{feeder}"
                ]

            for key in keys:
                if key == label:
                    errors.append(f"{label}: Node may not feed itself")
                elif key in seen_feeders:
                    errors.append(
                        f"{label}: duplicate resolved feeder {key!r}"
                    )
                elif key not in record_keys:
                    warnings.append(
                        f"{label}: feeder {feeder!r} has not been created"
                    )
                seen_feeders.add(key)

    return records, round_titles, errors, warnings


def table_cell(value: str) -> str:
    return html.escape(value or "").replace("|", "&#124;").replace("\n", " ")


def solution_link(record: dict[str, str]) -> str:
    if not record["has_solution"]:
        return ""
    round_id = quote(record["round"], safe="-_.~")
    directory = quote(record["directory"], safe="-_.~")
    return f"[solution](rounds/{round_id}/nodes/{directory}/solution.md)"


def feeder_coverage(round_records: list[dict[str, str]]) -> str:
    pool = {
        record["node_id"]: record
        for record in round_records
        if record["round_feeder"] == "yes"
    }
    consumers: dict[str, list[str]] = {node_id: [] for node_id in pool}
    unknown_metas: list[str] = []

    for meta in round_records:
        if meta["kind"] != "meta":
            continue
        feeders = parse_feeders(meta["feeders"])
        if feeders == ["unknown"]:
            unknown_metas.append(meta["node_id"])
            continue
        local_ids: set[str] = set()
        for feeder in feeders:
            pool_round = feeder_pool_round(feeder, meta["round"])
            if pool_round == meta["round"]:
                local_ids.update(
                    node_id
                    for node_id in pool
                    if node_id != meta["node_id"]
                )
            elif pool_round is None and "/" not in feeder and feeder in pool:
                local_ids.add(feeder)
        for node_id in local_ids:
            consumers[node_id].append(meta["node_id"])

    covered = [node_id for node_id, metas in consumers.items() if metas]
    unassigned = [node_id for node_id, metas in consumers.items() if not metas]
    shared = {
        node_id: metas
        for node_id, metas in consumers.items()
        if len(metas) > 1
    }

    parts = [f"{len(covered)}/{len(pool)}"]
    if unassigned:
        parts.append("unassigned: " + ", ".join(sorted(unassigned)))
    if shared:
        descriptions = [
            f"{node_id} → {', '.join(sorted(metas))}"
            for node_id, metas in sorted(shared.items())
        ]
        parts.append("shared: " + "; ".join(descriptions))
    if unknown_metas:
        parts.append("unknown Meta scope: " + ", ".join(sorted(unknown_metas)))
    return " · ".join(parts)


def render_summary(
    records: list[dict[str, str]],
    round_titles: dict[str, str],
) -> str:
    counts = Counter(record["status"] for record in records)
    progress = " · ".join(
        f"{counts[status]} {status}"
        for status in ALLOWED_STATUSES
        if counts[status]
    )

    lines = [
        "# Hunt Summary",
        "",
        "<!-- Generated by tools/build_summary.py. Do not edit manually. -->",
        "",
        f"**Overall:** {progress or 'No nodes yet'}",
        "",
    ]

    for round_id in sorted(round_titles, key=str.lower):
        title = round_titles[round_id]
        round_records = [
            record for record in records if record["round"] == round_id
        ]
        round_records.sort(key=lambda record: record["node_id"].lower())
        round_counts = Counter(record["status"] for record in round_records)
        round_progress = " · ".join(
            f"{round_counts[status]} {status}"
            for status in ALLOWED_STATUSES
            if round_counts[status]
        )

        lines.extend(
            [
                f"## {title} (`{round_id}`)",
                "",
                f"**Progress:** {round_progress or 'No nodes yet'}",
                "",
                f"**Feeder coverage:** {feeder_coverage(round_records)}",
                "",
                "| Kind | ID | Title | Pool | Parent | Status | Answer | Confidence | Feeders | Summary | Updated | Detail |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|",
            ]
        )

        for record in round_records:
            values = (
                record["kind"],
                record["node_id"],
                record["title"],
                record["round_feeder"],
                record["parent"],
                record["status"],
                record["answer"],
                record["confidence"],
                record["feeders"],
                record["summary"],
                record["updated"],
                solution_link(record),
            )
            lines.append(
                "| "
                + " | ".join(table_cell(value) for value in values)
                + " |"
            )
        lines.append("")

    return "\n".join(lines)


def update_summary() -> int:
    acquire_lock()
    temporary = ROOT / f".SUMMARY.{os.getpid()}.tmp"
    try:
        records, round_titles, errors, warnings = collect_records()
        if errors:
            print("Summary validation failed:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 2

        temporary.write_text(
            render_summary(records, round_titles),
            encoding="utf-8",
            newline="\n",
        )
        os.replace(temporary, SUMMARY)
    finally:
        if temporary.exists():
            temporary.unlink()
        release_lock()

    for warning in warnings:
        print(f"Warning: {warning}", file=sys.stderr)
    print(
        f"Updated {SUMMARY} with {len(records)} node(s) "
        f"in {len(round_titles)} round(s)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(update_summary())

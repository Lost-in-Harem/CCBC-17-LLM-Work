from __future__ import annotations

import argparse
import csv
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path

from bs4 import BeautifulSoup


@dataclass(frozen=True)
class Revision:
    timestamp: str
    editor: str
    comment: str


@dataclass(frozen=True)
class Transition:
    state: tuple[str, ...]
    rationale: str


def archived_index(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        return archive.read("index.html").decode("utf-8")


def extract_revisions(path: Path) -> list[Revision]:
    soup = BeautifulSoup(archived_index(path), "html.parser")
    newest_first: list[Revision] = []
    for item in soup.select(".sph-rev"):
        newest_first.append(
            Revision(
                timestamp=item.select_one(".sph-date").get_text(" ", strip=True),
                editor=item.select_one(".sph-user").get_text(" ", strip=True),
                comment=item.select_one(".sph-comment").get_text(" ", strip=True),
            )
        )
    return list(reversed(newest_first))


def build_transitions() -> list[Transition]:
    return [
        Transition(
            ("西湖", "先斩后奏", "显而易见", "家丁", "孙权", "岁月", "青提子"),
            "题面给出的初始七项。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "显而易见", "家人们", "孙权", "岁月", "青提子"),
            "复制‘先’、‘见’到首项前；家丁换成网络称呼‘家人们’。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "一清二楚", "家人们", "林冲", "岁月", "青提子"),
            "显而易见换同义成语；曹操之子曹林、曹冲的名组成林冲。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "一清二楚", "北家子们", "林冲", "岁月", "青提子"),
            "以‘子’替换近义的‘人’；首项的西顺时针转为北并前置。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "三明", "南家子", "林冲", "岁月", "青提子"),
            "一清二楚接续为福建三明；北取反为南并删去末字‘们’。",
        ),
        Transition(
            ("先斩后奏", "三明", "南家子", "雷横", "岁月", "青提子"),
            "林冲梁山座次第6，低19位为第25的雷横；再删首项。",
        ),
        Transition(
            ("先斩后奏", "三明", "南家子", "雷横", "刀", "青提子"),
            "岁月的常见比喻是刀（‘岁月是把杀猪刀’），并保持单字。",
        ),
        Transition(
            ("先提后斩", "三明", "南家子", "雷横", "刀", "青提子"),
            "先斩后奏交换第2、4字，再用青提子的中间字‘提’替换第2字。",
        ),
        Transition(
            ("先提后斩", "三明", "瓜", "雷横", "刀", "汁"),
            "南家子所需的合适字为‘瓜’，青提子所需的常见字为‘汁’；刀保持单字。",
        ),
        Transition(
            ("先提后斩", "三明", "瓜", "雷横", "切", "汁"),
            "刀前本可加动词‘切’，而‘切’可独立表示同一动作，故刀换为切。",
        ),
        Transition(
            ("三明", "汁", "横", "切", "瓜"),
            "交换倒数第4项与末项；删天气字‘雷’；删去四字项先提后斩。",
        ),
        Transition(
            ("JOHN", "横切南瓜"),
            "后三项归并为横切南瓜（jack-o'-lantern→JACK）；其余两项成三明汁≈三明治，追溯命名者John Montagu得JOHN；Jack亦是John昵称。",
        ),
        Transition(
            ("JOHN", "UNKNOWN_SURNAME"),
            "最新修改要求把末项换成合适姓氏；当前下载件没有改变后的第二版历史，姓氏仍未知。",
        ),
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    node = Path(__file__).resolve().parents[1]
    history_path = next((node / "input").glob("*历史修改记录*.html"))
    revisions = extract_revisions(history_path)
    if len(revisions) != 13:
        raise ValueError(f"Expected 13 revisions, found {len(revisions)}")

    day_numbers = [
        int(re.search(r"月(\d+)日", revision.timestamp).group(1))
        for revision in revisions
    ]
    date_message = "".join(chr(64 + number) for number in day_numbers)
    if date_message != "ITSREDHERRING":
        raise ValueError(f"Unexpected date message: {date_message}")

    transitions = build_transitions()
    if len(transitions) != len(revisions):
        raise ValueError("Transition count does not match revision count")

    output = args.output or Path(__file__).with_name("history_chain.tsv")
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            ["step", "timestamp", "editor", "state_after_edit", "rationale"]
        )
        for step, (revision, transition) in enumerate(
            zip(revisions, transitions), 1
        ):
            writer.writerow(
                [
                    step,
                    revision.timestamp,
                    revision.editor,
                    " | ".join(transition.state),
                    transition.rationale,
                ]
            )

    print(f"date signal: {date_message}")
    print("intermediate: JOHN")
    print("final surname: unresolved; altered history capture required")
    print(f"wrote: {output}")


if __name__ == "__main__":
    main()

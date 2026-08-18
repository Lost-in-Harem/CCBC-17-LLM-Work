from __future__ import annotations

import argparse
import csv
import html
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Revision:
    timestamp: str
    editor: str
    comment: str


@dataclass(frozen=True)
class Transition:
    state: tuple[str, ...]
    rationale: str


@dataclass(frozen=True)
class EditorClue:
    order: int
    category: str
    culture: str
    editor: str
    referent: str


DATE_RE = re.compile(r"^\d{4}年\d{1,2}月\d{1,2}日 \d{2}:\d{2}$")


def visible_lines(path: Path) -> list[str]:
    """Flatten the SingleFile capture into visible text lines (stdlib only)."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    text = re.sub(r"(?is)<br\s*/?>", "\n", text)
    text = re.sub(r"(?is)</(p|div|li|tr|h1|h2|h3|h4|td|section)>", "\n", text)
    text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", text))
    lines = (re.sub(r"[ \t\xa0]+", " ", line).strip() for line in text.split("\n"))
    return [line for line in lines if line]


def extract_revisions(path: Path) -> list[Revision]:
    """Read the revision list, which the page renders newest first."""
    lines = visible_lines(path)
    newest_first: list[Revision] = []
    for index, line in enumerate(lines):
        if not DATE_RE.match(line):
            continue
        editor = lines[index + 1]
        comment = lines[index + 2]
        if comment.startswith("（讨论"):
            comment = lines[index + 3]
        newest_first.append(
            Revision(timestamp=line, editor=editor, comment=comment)
        )
    return list(reversed(newest_first))


def build_transitions() -> list[Transition]:
    return [
        Transition(
            ("西湖", "先斩后奏", "显而易见", "家丁", "孙权", "岁月", "青提子"),
            "题面给出的初始七项。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "显而易见", "宅男", "孙权", "岁月", "青提子"),
            "复制‘先’、‘见’到首项前；第四项换成两字网络用语：家→宅、丁→男，得‘宅男’（提示长度核对 2→2）。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "一清二楚", "宅男", "林冲", "岁月", "青提子"),
            "显而易见换同义成语‘一清二楚’；曹操之子曹林、曹冲的名组成林冲。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "一清二楚", "北宅子", "林冲", "岁月", "青提子"),
            "青提子末字‘子’的近义字是‘男’，替换得‘宅子’；首项的方位‘西’顺时针转 90° 为‘北’并前置。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "三明", "南宅", "林冲", "岁月", "青提子"),
            "一清二楚接续为福建三明（一、二→三；清楚→明，提示长度核对 4→2）；北取反为南并删去第四项末字‘子’。",
        ),
        Transition(
            ("先斩后奏", "三明", "南宅", "雷横", "岁月", "青提子"),
            "林冲梁山座次第6，低19位为第25的雷横；再删首项。",
        ),
        Transition(
            ("先斩后奏", "三明", "南宅", "雷横", "梭", "青提子"),
            "岁月的常见比喻：岁月如梭，取‘梭’。",
        ),
        Transition(
            ("先提后斩", "三明", "南宅", "雷横", "梭", "青提子"),
            "先斩后奏交换第2、4字得先奏后斩，再用青提子的中间字‘提’替换第2字。",
        ),
        Transition(
            ("折", "三明", "南宅", "雷横", "梭", "青提子"),
            "取‘提’的前部扌与‘斩’的后部斤组成折（提示长度核对 4→1）；‘梭’本就是单字，正对应‘无论是否修改，须保持倒数第二个条目为单字’。",
        ),
        Transition(
            ("折", "三明", "南宅", "雷横", "穿", "青提子"),
            "梭前本应增加动词字‘穿’组成‘穿梭’；由于‘穿’单字本身即可表示同义动作，直接替换为‘穿’。",
        ),
        Transition(
            ("折", "横", "穿", "南宅"),
            "交换南宅与青提子；删天气字雷；青提子含月、日而删除；明含日、月，三明也按七曜规则删除。删雷后横、穿相邻成真词‘横穿’。",
        ),
        Transition(
            ("折", "横穿南宅"),
            "后三项横、穿、南宅按原序合并成四字条目‘横穿南宅’；合并之外只剩一个条目折，不触发剩余条目数量大于1的西文名称分支。",
        ),
        Transition(
            ("折", "毛"),
            "一‘横’‘穿’过‘宅’字‘南’（下）部的乇，乇加一横得‘毛’，且毛是合适姓氏（提示长度核对 4→1）；组合所有条目得到中间答案‘折毛’（用户确认正确）。",
        ),
    ]


def build_editor_clues() -> list[EditorClue]:
    return [
        EditorClue(1, "食物", "美国/英语", "什锦饭", "Jambalaya"),
        EditorClue(2, "人物", "德国/德语", "汉斯季默", "Hans Zimmer"),
        EditorClue(3, "人物", "美国/英语", "猫王", "Elvis Presley"),
        EditorClue(4, "作品", "俄罗斯/俄语", "罪与罚", "Crime and Punishment"),
        EditorClue(5, "食物", "俄罗斯/俄语", "罗宋汤", "Borscht"),
        EditorClue(6, "城市", "德国/德语", "法兰克福", "Frankfurt"),
        EditorClue(7, "人物", "俄罗斯/俄语", "柴可夫斯基", "Tchaikovsky"),
        EditorClue(8, "城市", "美国/英语", "巴吞鲁日", "Baton Rouge"),
        EditorClue(9, "城市", "俄罗斯/俄语", "圣彼得堡", "Saint Petersburg"),
        EditorClue(10, "食物", "德国/德语", "酸菜猪肘", "Sauerkraut pork knuckle"),
        EditorClue(
            11,
            "作品",
            "德国/德语",
            "变形记",
            "Die Verwandlung / The Metamorphosis（Franz Kafka）",
        ),
        EditorClue(
            12,
            "作品",
            "美国/英语",
            "百万英镑",
            "The Million Pound Bank Note（Mark Twain）",
        ),
    ]


def write_editor_grid(path: Path, clues: list[EditorClue]) -> None:
    if len(clues) != 12:
        raise ValueError(f"Expected 12 post-initial editors, found {len(clues)}")

    culture_next = {
        "美国/英语": "俄罗斯/俄语",
        "俄罗斯/俄语": "德国/德语",
        "德国/德语": "美国/英语",
    }
    category_next = {
        "食物": "人物",
        "人物": "城市",
        "城市": "作品",
        "作品": "食物",
    }

    rows: list[list[str | int]] = []
    anomalies: list[tuple[int, EditorClue, EditorClue]] = []
    for pair, (before, after) in enumerate(zip(clues[:6], clues[6:]), 1):
        expected_culture = culture_next[before.culture]
        expected_category = category_next[before.category]
        culture_ok = after.culture == expected_culture
        category_ok = after.category == expected_category
        if not (culture_ok and category_ok):
            anomalies.append((pair, before, after))

        resolution = "-"
        shared_letters = ""
        repaired_person = ""
        if pair == 5:
            # The folded pair is the only category mismatch.  It is recorded as
            # a plain observation only: every extraction tried on this cell so
            # far (the work title, its author, the already-used German person,
            # and the BORSCHT/THEMETAMORPHOSIS shared letters) was rejected by
            # the user, and the mismatch is in fact forced by the design (see
            # solution.md, "Editor grid: closed route"), so it carries no
            # answer.
            left = re.sub(r"[^A-Z]", "", before.referent.upper())
            right = re.sub(r"[^A-Z]", "", after.referent.upper())
            shared_letters = "".join(sorted(set(left).intersection(right)))
            repaired_person = ""
            resolution = (
                "唯一类别异常：按循环这里应为德国人物；变形记是德语作品。"
                "该异常由排列本身强制产生，所有基于它的抽取均已被用户判错。"
            )

        rows.append(
            [
                pair,
                before.order,
                before.editor,
                before.referent,
                before.culture,
                before.category,
                after.order,
                after.editor,
                after.referent,
                after.culture,
                after.category,
                expected_culture,
                expected_category,
                "ok" if culture_ok else "mismatch",
                "ok" if category_ok else "mismatch",
                shared_letters,
                repaired_person,
                resolution,
            ]
        )

    if len(anomalies) != 1:
        raise ValueError(f"Expected one editor-pair anomaly, found {anomalies}")
    pair, before, after = anomalies[0]
    if (pair, before.editor, after.editor) != (5, "罗宋汤", "变形记"):
        raise ValueError(f"Unexpected editor-pair anomaly: {anomalies[0]}")

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "pair",
                "before_order",
                "before_editor",
                "before_referent",
                "before_culture",
                "before_category",
                "after_order",
                "after_editor",
                "after_referent",
                "after_culture",
                "after_category",
                "expected_after_culture",
                "expected_after_category",
                "culture_check",
                "category_check",
                "shared_letters",
                "repaired_person",
                "resolution",
            ]
        )
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--editor-output", type=Path)
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

    editor_clues = build_editor_clues()
    recorded_editors = [revision.editor for revision in revisions]
    if recorded_editors[0] != "中国队长":
        raise ValueError(f"Unexpected initial editor: {recorded_editors[0]}")
    if recorded_editors[1:] != [clue.editor for clue in editor_clues]:
        raise ValueError("Editor clues do not match the archived chronological order")

    editor_output = args.editor_output or Path(__file__).with_name(
        "editor_grid.tsv"
    )
    write_editor_grid(editor_output, editor_clues)

    print(f"date signal: {date_message}")
    print("date verdict: a notice that the dates are a red herring")
    print("intermediate answer (user-confirmed): 折毛")
    print("second phase: delete the four Russian-editor records and replay;")
    print("final answer is English and is still open (see solution.md)")
    print(f"wrote: {output}")
    print(f"wrote: {editor_output}")


if __name__ == "__main__":
    main()

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


@dataclass(frozen=True)
class EditorClue:
    order: int
    category: str
    culture: str
    editor: str
    referent: str


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
            ("先见西湖", "先斩后奏", "显而易见", "人设", "孙权", "岁月", "青提子"),
            "复制‘先’、‘见’到首项前；第四项换成两字网络用语‘人设’。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "一清二楚", "人设", "林冲", "岁月", "青提子"),
            "显而易见换同义成语；曹操之子曹林、曹冲的名组成林冲。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "一清二楚", "北子设", "林冲", "岁月", "青提子"),
            "以‘子’替换‘人设’中的近义字‘人’；首项的西顺时针转为北并前置。",
        ),
        Transition(
            ("先见西湖", "先斩后奏", "三明", "南子", "林冲", "岁月", "青提子"),
            "一清二楚接续为福建三明；北取反为南并删去第四项末字‘设’，得到历史人物南子。",
        ),
        Transition(
            ("先斩后奏", "三明", "南子", "雷横", "岁月", "青提子"),
            "林冲梁山座次第6，低19位为第25的雷横；再删首项。",
        ),
        Transition(
            ("先斩后奏", "三明", "南子", "雷横", "杀猪刀", "青提子"),
            "岁月的常见比喻是‘杀猪刀’。此步尚未要求倒数第二项保持单字。",
        ),
        Transition(
            ("先提后斩", "三明", "南子", "雷横", "杀猪刀", "青提子"),
            "先斩后奏交换第2、4字，再用青提子的中间字‘提’替换第2字。",
        ),
        Transition(
            ("折", "三明", "南子", "雷横", "刻", "青提子"),
            "按提示的 4→1 约束，取‘提’的前部扌与‘斩’的后部斤组成折；三明与南子都是已有的完整条目而无需改动；‘杀猪刀’按亥（猪）+刂（刀）组成刻，满足倒数第二项保持单字。",
        ),
        Transition(
            ("折", "三明", "南子", "雷横", "雕", "青提子"),
            "刻前增加表示动作的‘雕’组成‘雕刻’；由于‘雕’单字本身即可表示同义动作，直接用雕替换刻。",
        ),
        Transition(
            ("折", "横", "雕", "南子"),
            "交换南子与青提子；删天气字雷；青提子含月、日而删除；明含日、月，三明也按七曜规则删除。",
        ),
        Transition(
            ("折", "横雕南子"),
            "后三项横、雕、南子按原序合并成四字条目‘横雕南子’；合并之外只剩一个条目折，不触发剩余条目数量大于1的西文名称分支。",
        ),
        Transition(
            ("折", "子"),
            "按4→1提示将四字末项‘横雕南子’换成单字姓氏‘子’：南子是宋国子姓女子；组合所有条目得到中间答案‘折子’。",
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
            # The folded pair is the only category mismatch.  Its English
            # referents have a deliberately useful multiset intersection:
            # BORSCHT ∩ THEMETAMORPHOSIS = H,O,R,S,T.  Alphabetically writing
            # that overlap gives HORST, a German male given name, which fits
            # the missing German-person slot.  Keep the extraction explicit so
            # the candidate is reproducible rather than an arbitrary title or
            # author guess.
            left = re.sub(r"[^A-Z]", "", before.referent.upper())
            right = re.sub(r"[^A-Z]", "", after.referent.upper())
            shared_letters = "".join(
                sorted(set(left).intersection(right))
            )
            repaired_person = "HORST" if shared_letters == "HORST" else ""
            resolution = (
                "唯一类别异常：按循环这里应为德国人物；变形记是德语作品。"
                f"其英文名与 Borscht 的共有字母为 {shared_letters}，"
                f"重排成德国人名 {repaired_person}"
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
    print("history result / intermediate: 折子 (folded-history instruction)")
    print("milestone bridge: final editor is The Million Pound Bank Note")
    print("paired-editor anomaly: Borscht -> The Metamorphosis")
    print("expected second type: German-language person")
    print("folded overlap: BORSCHT ∩ THEMETAMORPHOSIS = HORST")
    print("answer candidate: HORST (German-person repair; not submitted)")
    print(f"wrote: {output}")
    print(f"wrote: {editor_output}")


if __name__ == "__main__":
    main()

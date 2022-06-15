#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: subtitle_processing.py
Created: Thursday, 2nd December 2021 10:55:36 AM

Last Modified: Friday, 1st April 2022 4:02:32 PM

Summary: 

"""
import re
from pathlib import Path


def clean_raw_subs(text):
    # transformations that should be done to the raw SRT data, before the subs are manually corrected
    # remove the lines containing only digits (some kind of counter)
    text = re.sub("(\n|^)\d+\n", "\n", text)
    # remove styling tags
    text = re.sub("<.*?>", "", text)
    text = re.sub(
        r"(?<!,|\n) ?\b((and)|(or)|(but)|(so))\b", r", \1", text
    )  # punctuate conjunctions #TODO test this to make sure it's not too inefficient

    mapping_dict = {
        "coriander": "Coriander",
        "corriander": "Coriander",
        "janar": "Donaar",
        "dinar": "Donaar",
        r"\bdenar": "Donaar",
        "rosie": "Rosie",
        "rosy": "Rosie",
        "bee stinger": "Beestinger",
        "bee stringer": "Beestinger",
        "cthe wrist": "K'thriss",
        r"\boak\b": "Oak",
        r"\boke\b": "Oak",
        "brahma": "Brahma",
        "walnut": "Walnut",
        "Blitzen": "Blit'zen",
        "blitz in": "Blit'zen",
        "dark magic": "Darkmagic",
        "acquisitions incorporated": "Acquisitions Incorporated",
        "Cupid": "Kiupid",
        "true strike": "Truestrike",
        "\bomen": "Omin",
        "Lysander": "Lathander",
        r"\bi\b": "I",
        r"\brebus\b": "Driebus",
        "drivas": "Driebus",
        r"\b\revis\b": "Driebus",
        r"(?:W|w)alnut.{,7}(\n^[\n\d\-:>\s,]{,30})?grass": r"Walnut Dankgrass\1",
        "(S|s)hadow (C|c)ouncil": "Shadow Council",
        "head office": "Head Office",
        "sebastian": "Sebastian",
        "(C|c|(see)).?(T|t)eam": "C-Team",
        "(B|b|(bee)).?(T|t)eam": "B-Team",
        "test market": "Test Market",
        "Carthoris": "K'thriss",
        "&amp;":"&"
    }

    for pattern, repl in mapping_dict.items():
        text = re.sub(pattern, repl, text)
    # test this
    # text = re.sub(r"walnut[^\n]+?(\n+[\d: ->,]+?\n+)?grass", r"Walnut Dankgrass\1", text, flags=re.DOTALL)
    return text


def clean_formatted_text(text):
    # for making any final corrections to the text after it has been manually cleaned and corrected.
    # TODO: replace ... string with \cdots for Latex
    # TODO: replace any \amy with \trystan
    mapping_dict = {"\amy\b": "\trystan", "...": "\cdots"}
    pass


if __name__ == "__main__":
    file_path = Path(
        r"C:\Users\Ryan.Mai\Documents\Other\cteam_transcriptions\subtitles\Plans Within Plans, Part 1 - S2 E02 - Acquisitions Inc_ The _C_ Team (1080p_30fps_H264-128kbit_AAC).English.srt"
    )
    with open(file_path) as f:
        text = f.read()
        clean_text = clean_raw_subs(text)
    with open(file_path.parent / "clean_subtitles" / file_path.stem, "w") as f:
        f.write(clean_text)

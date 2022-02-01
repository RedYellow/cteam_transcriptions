#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: utils.py
Created: Tuesday, 14th December 2021 9:24:06 AM

Last Modified: Friday, 17th December 2021 5:18:16 PM

Summary: 

"""
import re


def load_srt_to_dict(file_path):
    with open(file_path, "r") as f:
        text = f.read()
        matches = re.findall("\n([\d: -=>,]+)\n(.*?)", text)
    return {match[0]: match[1] for match in matches}


if __name__ == "__main__":
    x = load_srt_to_dict(
        r"cteam_transcriptions\subtitles\clean_subtitles\Acq Inc_ The _C_ Team Live - PAX South 2018 (1080p_60fps_H264-128kbit_AAC).English.srt"
    )
    print(x)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:56:37 2021

@author: Nic
"""

import pysrt
import re

def ts_to_secs(ts):
    hours, mins, secs, ms = ts
    return 3600*hours+mins*60+secs

ex_sub = "Acq Inc_ The “C” Team_ Plans Within Plans (abridged) (1080p_30fps_H264-128kbit_AAC).English.srt"

subs = pysrt.open("./subtitles/{}".format(ex_sub))

text = []

for subt in subs:
    text.append(re.sub("</?.*?>", "", subt.text))

with open("x.txt", "w") as f:
    f.write("\n".join(text))
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: subtitle_processing.py
Created: Thursday, 2nd December 2021 10:55:36 AM

Last Modified: Friday, 3rd December 2021 1:38:56 PM

Summary: 

"""
import re


def clean_subs(text):
    # remove the lines containing only digits (some kind of counter)
    text = re.sub("(\n|^)\d+\n", "\n", text)
    # remove styling tags
    text = re.sub("<.*?>", "", text)
    text = re.sub(
        "[^,] ((?:but)|(?:and)) ", ", \1 ", text
    )  # punctuate conjunctions #TODO test this to make sure it's not too inefficient

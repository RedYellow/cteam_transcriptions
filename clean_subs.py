#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: subtitle_processing.py
Created: Thursday, 2nd December 2021 10:55:36 AM

Last Modified: Thursday, 2nd December 2021 10:59:29 AM

Summary: 

"""
import re


def clean_subs(text):
    text = re.sub(
        "(\n|^)\d+\n", "\n", text
    )  # remove the lines containing only digits (some kind of counter)
    text = re.sub("<.*?>", "", text)

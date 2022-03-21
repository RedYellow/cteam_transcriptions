#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:09:01 2021

@author: Nic
"""

import pdflatex
import yaml
from pylatex import Command, Document, Section, Subsection, UnsafeCommand
from pylatex.base_classes import Arguments, CommandBase, Environment
from pylatex.package import Package
from pylatex.utils import NoEscape, italic


def split_lines_by_speaker():
    # timestamp_lines should be a dictionary (DefaultDict?) of timestamp:lines (both str)
    # If a single speaker's lines goes over multiple timestamps, I want to get only the first one
    # so {"00:01":"\dm blah blah", {"00:10":"blah blah \n\someoneelse blah blah"}}
    pass


def create_dram_per(doc, char_reg_file):
    # get list of characters appearing in script
    # match to character_registry.yaml
    # create DramPer based on that
    # ? hyperlink speaker tags back to the DramPer section?
    # ? create a table for the characters? including player name, description etc?
    # which characters should be included? all characters? including DMPCs?
    
    # * this should only include characters that appear in the episode, while the character registry file will contain all characters
    #* show a warning if a character appears in the text but not the char registry
    # with open(char_reg_file, "r") as f:
    #     char_info = yaml.safe_load(f)
    # for char in char_info.items():
    #     doc.append(
    #         Command("Character", arguments=["fae", "fae"], options=char["fullname"])
    #     )


def generate_document(timestamp_lines):
    # timestamp_lines should be a dictionary (DefaultDict?) of timestamp:lines (both str)

    for ts, line_chunk in timestamp_lines.items():
        pass


def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    doc.packages.append(Package("dramatist"))
    doc.append(Command("Character", arguments=["fae", "fae"], options="fae"))
    doc.append(Command("DramPer"))
    with doc.create(Environment("drama")):
        doc.append(Command("\faespeaks"))
    # with doc.create(Section("A section")):
    #     doc.append("Some regular text and some ")
    #     doc.append(italic("italic text. "))
    #     doc.append("")
    #     with doc.create(Subsection("A subsection")):
    #         doc.append("Also some crazy characters: $&#{}")
    return doc


if __name__ == "__main__":
    # Basic document
    doc = Document("basic")
    doc = fill_document(doc)

    doc.generate_pdf(clean_tex=False, compiler="latexmk")
    doc.generate_tex()

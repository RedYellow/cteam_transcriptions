#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:09:01 2021

@author: Nic
"""

from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
from pylatex.package import Package
from pylatex import Document, Section, UnsafeCommand
from pylatex.base_classes import Environment, CommandBase, Arguments

import pdflatex

def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    doc.packages.append(Package('dramatist'))

    with doc.create(Section('A section')):
        doc.append('Some regular text and some ')
        doc.append(italic('italic text. '))

        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')


if __name__ == '__main__':
    # Basic document
    doc = Document('basic')
    fill_document(doc)

doc.generate_pdf(clean_tex=False, compiler="latexmk")
doc.generate_tex()

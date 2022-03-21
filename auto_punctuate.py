#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: auto_punctuate.py
Created: Tuesday, 15th March 2022 3:06:41 PM
Author: ryan.mai (ryan.mai@medwatchers.com)

Last Modified: Wednesday, 16th March 2022 9:25:09 AM
Modified By: ryan.mai (ryan.mai@medwatchers.com)

Summary: 

"""
############
from nemo.collections.nlp.models import PunctuationCapitalizationModel
from transformers import T5ForConditionalGeneration, T5Tokenizer

# model_name = "flexudy/t5-small-wav2vec2-grammar-fixer"

# tokenizer = T5Tokenizer.from_pretrained(model_name)

# model = T5ForConditionalGeneration.from_pretrained(model_name)

# sent = """she's okay but i'm not crazy about her methods. from outfitter and relic enthusiast moral we acquired drow  disguises for entry into guallidurth  and they could not have been worse disguises but they did transmute tasty into tasteful who got a heaping helping of that savory meat anyway house rah'uuthli  my former home had fallen into such disfavor that the city condemned it to reclamation by the wilds of the underdark its ruins now home to a host of driders one of which had been my mother"""

# input_text = "fix: { " + sent + " } </s>"

# input_ids = tokenizer.encode(
#     input_text,
#     return_tensors="pt",
#     max_length=256,
#     truncation=True,
#     add_special_tokens=True,
# )

# outputs = model.generate(
#     input_ids=input_ids,
#     max_length=256,
#     num_beams=4,
#     repetition_penalty=1.0,
#     length_penalty=1.0,
#     early_stopping=True,
# )

# sentence = tokenizer.decode(
#     outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True
# )

# print(f"{sentence}")

# She's okay, but I'm not crazy about her methods. From outfitter andlic enthusiast moral, we acquired drow disguises for entry into Guallidurth, and they could not have been worse disguises, but they did transmute tasty into tasteful, who got a heaping helping of that sweet meat anyway. Haus Rah'uuthli, my former home, had fallen into such disfavor that the city condemned it to reclamation by the wilds of the underdark. Its ruins now home to a host of addicts, one of which had been my mother.


# to get the list of pre-trained models
PunctuationCapitalizationModel.list_available_models()

# Download and load the pre-trained BERT-based model
model = PunctuationCapitalizationModel.from_pretrained("punctuation_en_bert")

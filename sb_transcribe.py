#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:54:00 2021

@author: Nic
"""

from speechbrain.pretrained import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-rnnlm-librispeech", savedir="pretrained_models/asr-crdnn-rnnlm-librispeech")
print("loaded model")
asr_model.transcribe_file('/Users/Nic/Documents/Python Projects/cteam_transcriptions/audio/Acq Inc_ The “C” Team_ Plans Within Plans (abridged) (192kbit_AAC).wav')

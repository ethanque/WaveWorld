#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 23:52:22 2022

@author: ethanque
"""



import numpy as np
from scipy.io.wavfile import write
import sys
sys.path.append('..')
from Utilities.sinSqEnv import sinSqEnv

samplingRate = 44100
fileLength = 30
numSamples = fileLength*samplingRate
x = np.arange(numSamples)
t = x/samplingRate
y = np.zeros(numSamples)

pitchesPerSecond = 3

startFreq = 100
freq = startFreq
freqMult = 1.2
maxFundamentalFreq = 1280

envRise = .2
pitchDuration = 5
envFade = 1.5

tStart = 0.1 - 1/pitchesPerSecond
tGone = 0
while tGone < (fileLength-2):
    freq = freq*freqMult
    if freq > maxFundamentalFreq:
        freq = np.mod(freq,startFreq)
    tStart = tStart + 1/pitchesPerSecond
    tReach = tStart + envRise
    tGone = tStart + pitchDuration
    tFade = tGone - envFade
    firstSample = int(np.floor(tStart*samplingRate)-1)
    tFirstSample = firstSample/samplingRate
    lastSample = int(np.ceil(tGone*samplingRate)+1)
    numSamples = lastSample - firstSample
    yAdd = np.sin(2*np.pi*freq*t[firstSample:lastSample])\
        *sinSqEnv(tStart, tReach, tFade, tGone, tFirstSample, numSamples, samplingRate)
    y[firstSample:lastSample] = y[firstSample:lastSample] + yAdd
    

scaled = np.int16(y/np.max(np.abs(y)) * 32767)
write('../Data/test.wav', 44100, scaled)
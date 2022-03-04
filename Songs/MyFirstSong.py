#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:53:23 2022

@author: ethanque
"""



import numpy as np
from scipy.io.wavfile import write
import sys
sys.path.append('..')
from Utilities.sinSqEnv import sinSqEnv

samplingRate = 44100
fileLength = 5
numSamples = fileLength*samplingRate
x = np.arange(numSamples)

freq = 100
amp = 100
y = amp*np.sin(2*np.pi*freq*x/samplingRate)
for m in range(32):
    freq = freq+freq*0.6
    amp = amp*0.618034
    y = y + amp*np.sin(2*np.pi*freq*x/samplingRate)

tStart = 0.1
tReach = 1
tFade = fileLength - 2
tGone = fileLength - 0.5
tFirstSample = 0
y = np.multiply(y, sinSqEnv(tStart,tReach,tFade,tGone,tFirstSample,numSamples,samplingRate))

scaled = np.int16(y/np.max(np.abs(y)) * 32767)
write('../Data/test.wav', 44100, scaled)
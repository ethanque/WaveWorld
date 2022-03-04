#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:59:24 2022

@author: ethanque
"""

from numpy import linspace, cos, pi

def sinSqEnv(tStart,tReach,tFade,tGone,tFirstSample,numSamples,samplingRate):
    # Time at the beginning of the last sample
    tLastSample = tFirstSample + (numSamples-1)/samplingRate
    # Time array
    timeArray = linspace(tFirstSample,tLastSample,numSamples)
    # Initialize amplitudesArray
    amplitudesArray = 0*timeArray
    # Effective frequency during rise
    omegaRise = pi/(tReach-tStart)
    phi0Rise = -omegaRise*tStart
    # Effective frequency during fall
    omegaFall = pi/(tGone-tFade)
    phi0Fall = pi-omegaFall*tFade
    
    for m in range(0,numSamples):
        if tReach <= timeArray[m] and timeArray[m] <= tFade:
            amplitudesArray[m] = 1
        elif tStart <= timeArray[m] and timeArray[m] < tReach:
            amplitudesArray[m] = 0.5*(1-cos(omegaRise*timeArray[m]+phi0Rise))
        elif tFade < timeArray[m] and timeArray[m] <= tGone:
            amplitudesArray[m] = 0.5*(1-cos(omegaFall*timeArray[m]+phi0Fall))
            
    return amplitudesArray
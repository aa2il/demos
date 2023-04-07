#!/usr/bin/python3

# Basic example to test soapy SDR python bindings

import SoapySDR
from SoapySDR import *
import numpy 

#enumerate devices
results = SoapySDR.Device.enumerate()
for result in results: print('\n',result)

#create device instance
#args can be user defined or from the enumeration result
args = dict(driver="rtlsdr")
sdr = SoapySDR.Device(args)

#query device info
print('\nAntennas=',sdr.listAntennas(SOAPY_SDR_RX, 0))
print('Gains=',sdr.listGains(SOAPY_SDR_RX, 0))
freqs = sdr.getFrequencyRange(SOAPY_SDR_RX, 0)
for freqRange in freqs:
    print('Freq Range=',freqRange)

#apply settings
sdr.setSampleRate(SOAPY_SDR_RX, 0, 1e6)
sdr.setFrequency(SOAPY_SDR_RX, 0, 912.3e6)

#setup a stream (complex floats)
rxStream = sdr.setupStream(SOAPY_SDR_RX, SOAPY_SDR_CF32)
sdr.activateStream(rxStream) #start streaming

#create a re-usable buffer for rx samples
buff = numpy.array([0]*1024, numpy.complex64)

#receive some samples
for i in range(10):
    sr = sdr.readStream(rxStream, [buff], len(buff))
    print('\nNo. samps  =',sr.ret)    #num samples or error code
    print('Flags      =',sr.flags)  #flags set by receive operation
    print('Time Stamp =',sr.timeNs) #timestamp for receive buffer
    print('Last buffer=',buff)
    
#shutdown the stream
sdr.deactivateStream(rxStream) #stop streaming
sdr.closeStream(rxStream)

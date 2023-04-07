#! /usr/bin/python3

# Script to play with async streaming in pyrtlsdr

# pip3 install pyrtlsdr

# Read and print some samples

import sys
import time
import asyncio
from rtlsdr import RtlSdr

sdr = RtlSdr()

async def streaming():

    async for samples in sdr.stream():
        # do something with samples
        print(samples[0:10],len(samples))

    # to stop streaming:
    await sdr.stop()

    # done
    sdr.close()

#loop = asyncio.get_event_loop()
#loop.run_until_complete(streaming())
asyncio.run(streaming())

while True:
    print('Tic ...')
    time.sleep(1)

sys.exit(0)

async def main():
    import math

    sdr = RtlSdr()

    print('Configuring SDR...')
    sdr.rs = 2.4e6
    sdr.fc = 100e6
    sdr.gain = 10
    print('  sample rate: %0.6f MHz' % (sdr.rs/1e6))
    print('  center frequency %0.6f MHz' % (sdr.fc/1e6))
    print('  gain: %d dB' % sdr.gain)

    print('Streaming samples...')

    i = 0
    async for samples in sdr.stream():
        power = sum(abs(s)**2 for s in samples) / len(samples)
        print('Relative power:', 10*math.log10(power), 'dB')

        i += 1

        if i > 100:
            sdr.stop()
            break

    print('Done')

    sdr.close()


main()




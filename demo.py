#!/usr/bin/env python3
import socket
import time
from sys import exit, stdout, path
from functools import partial

from demo.composer import Composer
from chordtable.chordtable import Chordtable
from chordtable.misc import format_fudi

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))

chord = Chordtable()
crap_composer = Composer()

while True:
    p, delta = chord.next_step()

    if delta > 0 and not (chord.weights[p] < chord.max_weight):
        continue

    chord = chord.modify((p, delta))
    print(format_fudi(*chord.weights).decode('ascii'))

    for _ in range(0, 3):
        if delta > 0:
            crap_composer.weight(p)
        else:
            crap_composer.lighten(p)

    for beat in range(0, 24):
        for voice, staff in enumerate(crap_composer.staves):
            s.sendall(format_fudi(
                voice + 1,
                staff[beat].pitch,
                staff[beat].params[0],
                staff[beat].params[1]
            ))
        time.sleep(0.125)

import sys
import time

import navio.rcinput
import navio.util

navio.util.check_apm()

rcin = navio.rcinput.RCInput()

period = []

while (True):
    period.append(rcin.read(0))
    period.append(rcin.read(1))
    period.append(rcin.read(2))
    period.append(rcin.read(3))
    period.append(rcin.read(4))
    period.append(rcin.read(5))
    period.append(rcin.read(6))
    period.append(rcin.read(7))
    print(period)

# import sys
# import time

import navio.rcinput
import navio.util

# navio.util.check_apm()

rcin = navio.rcinput.RCInput()

period = {"0": None, "1": None, "2": None, "3": None, "4": None, "5": None, "6": None, "7": None, }
period2 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, }

while (True):

    for t in period2:
        period[t] = rcin.read(int(t))

    print(period)

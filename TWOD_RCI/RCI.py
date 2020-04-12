
from TWOD_NA2.rcinput import *
from TWOD_NA2.util import *

check_apm()

from RCI_ENC import *

rcin = RCInput()


# def rci(rc_channl):
#     return int(rcin.read(rc_channl))

def rci(rc_channl):
    rc_rx = int(rcin.read(rc_channl))
    h = rci_enc(rc_rx)
    return h

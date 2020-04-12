
from TWOD_NA2.rcinput import *
from TWOD_NA2.util import *
from RCI_ENC import *

check_apm()

rcin = RCInput()


def rci(rc_channl):
    return rci_enc(float(rcin.read(rc_channl)))

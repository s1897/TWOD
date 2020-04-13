
from TWOD_NA2.rcinput import *
from TWOD_NA2.util import *
from TWOD_RCI.RCI import *

check_apm()

rcin = RCInput()


# def rci(rc_channl):
#     return rci_enc(float(rcin.read(rc_channl)))

def rci(rc_cn):
    return rie(float(rcin.read(rc_channl)))

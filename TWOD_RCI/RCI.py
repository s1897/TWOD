
from TWOD_NA2.rcinput import RCInput
from TWOD_NA2.util import check_apm

check_apm()

from RCI_ENC import rci_enc

return(int(RCInput().read(1)))

# def rci(rc_channl, rc_drx=-1, rc_urx=1, rc_di=982, rc_ui=2006):
#     return rci_enc(int(RCInput().read(rc_channl)), rc_drx, rc_urx, rc_di, rc_ui)

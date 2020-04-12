
from TWOD_NA2.rcinput import RCInput as ri
from TWOD_NA2.util import check_apm

check_apm()

from RCI_ENC import rci_enc


def rci(rc_channl, rc_drx=-1, rc_urx=1, rc_di=982, rc_ui=2006):
    return rci_enc(int(ri.read(rc_channl)), rc_drx, rc_urx, rc_di, rc_ui)

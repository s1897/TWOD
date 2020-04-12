
def rci_enc(rc_rx, rc_drx, rc_urx, rc_di, rc_ui):

    rc_sr = rc_ui - rc_di

    return (((rc_urx - rc_drx) / rc_sr) * (rc_sr - (rc_ui - rc_rx))) + rc_drx

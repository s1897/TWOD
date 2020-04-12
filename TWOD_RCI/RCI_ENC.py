

def rci_enc(rc_rx, rc_drx=-1, rc_urx=1, rc_di=982, rc_ui=2006):
    print(rc_rx)

    rc_sr = rc_ui - rc_di

    return (((rc_urx - rc_drx) / rc_sr) * (rc_sr - (rc_ui - rc_rx))) + rc_drx


if __name__ == '__main__':
    print(rci_enc((2006 - 982) / 2 + 982))



def rci_enc(rc_rx, rc_drx=-1, rc_urx=1, rc_di=982, rc_ui=2006):

    rc_sr = rc_ui - rc_di

    print(rc_rx + 1000, (((rc_urx - rc_drx) / rc_sr) * (rc_sr - (rc_ui - rc_rx))) + rc_drx)
    # return (((rc_urx - rc_drx) / rc_sr) * (rc_sr - (rc_ui - rc_rx))) + rc_drx


if __name__ == '__main__':
    print(rci_enc(int(1400)))
    print(rci_enc(int(982)))

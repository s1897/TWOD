
def rci_enc(rtx, drtx=-1, urtx=1, dsr=982, usr=2006):

    rsr = usr - dsr

    return (((urtx - drtx) / rsr) * (rsr - (usr - rtx))) + drtx


if __name__ == '__main__':
    print(rci_enc(982))

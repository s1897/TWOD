def rci_enc(rtx, drtx=-1, urtx=1, dsr=982, usr=2006):

    return ((((abs(drtx) + urtx) / (usr - dsr)) * (int(rtx) - dsr)) + drtx)


if __name__ == '__main__':
    rci_enc(2006)

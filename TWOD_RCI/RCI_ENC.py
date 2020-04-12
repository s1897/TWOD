def rci_enc(rtx, drtx=-1, urtx=1, dsr=982, usr=2006):

    if rtx == 982:
        print(True)

    print((((abs(drtx) + urtx) / (usr - dsr)) * (rtx - dsr)) + drtx)
    print(int(rtx))


if __name__ == '__main__':
    print("")

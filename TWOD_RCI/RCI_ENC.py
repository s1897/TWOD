def rci_enc(rtx, drtx=-1, urtx=1, dsr=982, usr=2006):

    print((((abs(drtx) + urtx) / (usr - dsr)) * (int(rtx) - dsr)) + drtx)
    print(int(rtx) + 5 / 20000)


if __name__ == '__main__':
    print("")


# ██████  ██ ███████
# ██   ██ ██ ██
# ██████  ██ █████
# ██   ██ ██ ██
# ██   ██ ██ ███████

# rie = receiver imput encoder
#
# rri   = raw receiver imput
# elo   = encoder lowest output
# eho   = encoder highest outout
# lsr   = lowest step range
# hsr   = highest step range
# tsr   = total step range
# sss   = single step size
# mss   = multiplier step size
# rte   = return the encode


def rie(rri, elo=-1, eho=1, lsr=982, hsr=2006):

    # calculates total step range
    tsr = hsr - lsr

    # calculates a single step size with the total step range and the lowest and highest encoder output
    sss = (eho - elo) / tsr

    # calculates the multiplier step size with total step range and the highest encoder output and the raw resiver imput
    mss = tsr - (hsr - rri)

    # multiplie single step size whit multiplier step size and add encoder lowest output
    rte = sss * mss + elo

    # return the encode receiver imput
    return rte


if __name__ == '__main__':
    print(rci_enc(1494))

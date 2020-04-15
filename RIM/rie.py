
# ██████  ██ ███████
# ██   ██ ██ ██
# ██████  ██ █████
# ██   ██ ██ ██
# ██   ██ ██ ███████

# rie = receiver imput encoder, takes the raw input of the receiver and converts it to specified values
#
#
# rir   = raw imput receiver
# elo   = encoder lowest output
# eho   = encoder highest outout
# lsr   = lowest step range
# hsr   = highest step range
# tsr   = total step range
# sss   = single step size
# mss   = multiplier step size
# eri   = encodet receiver imput
#
#


# define receiver imput encoder
def rie(rir, elo=-1, eho=1, lsr=982, hsr=2006):

    # calculates total step range
    tsr = hsr - lsr

    # calculates a single step size with the total step range and the lowest and highest encoder output
    sss = (eho - elo) / tsr

    # calculates the multiplier step size with total step range and the highest encoder output and the raw resiver imput
    mss = tsr - (hsr - rir)

    # multiplie single step size whit multiplier step size and add encoder lowest output
    eri = sss * mss + elo

    # returns encodet receiver imput
    return eri


if __name__ == '__main__':
    print(rci_enc(1494))

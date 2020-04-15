
# ██████  ██████  ██████
# ██   ██ ██   ██ ██   ██
# ██████  ██████  ██████
# ██   ██ ██   ██ ██
# ██   ██ ██   ██ ██

# rrp = register receiver psition
#
#
# rca = receiver cannal amount
# rsn = register string name
# rpd = register psition directory
# rpn = receiver psition name
# sle = string length encoder
#
#


# define register receiver channels
def rrp(rca=8):

    # converts receiver channel amount to string length encoder
    sle = str(len(list(str(rca))) + 1)

    # construct identification string name
    rsn = "rpn_{:0" + sle + "d}"

    # construct register string director
    rpd = dict(map(lambda x: (rsn.format(x), None), range(rca)))

    return rpd


if __name__ == '__main__':
    print(rrp())

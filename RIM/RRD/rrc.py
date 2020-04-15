
# ██████  ██████   ██████
# ██   ██ ██   ██ ██
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██   ██ ██   ██  ██████

# rrc = register receiver channels
#
#
# rca = receiver cannal amount
# rsn = register string name
# rcd = register cannal directory
# rcn = receiver cannal name
# sle = string length encoder
#
#


# define register receiver channels
def rrc(rca=8):

    # converts receiver channel amount to string length encoder
    sle = str(len(list(str(rca))) + 1)

    # construct identification string name
    rsn = "rcn_{:0" + sle + "d}"

    # construct register string director
    rcd = dict(map(lambda x: (rsn.format(x), None), range(rca)))

    return rcd


if __name__ == '__main__':
    print(rrc())

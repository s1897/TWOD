
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██   ██ ██   ██ ██

# rri = register reciver imput
#
# rca = receiver cannal amount
# rsn = register string name
# rid = register imput directory
# rin = receiver imput name
# sle = string length encoder
#
#

# define register reciver imput


def rri(rca=8):

    # converts receiver channel amount to string length encoder
    sle = str(len(list(str(rca))) + 1)

    # construct identification string name
    rsn = "rin_{:0" + sle + "d}"

    # construct register string director
    rid = dict(map(lambda x: (rsn.format(x), None), range(rca)))

    return rid


if __name__ == '__main__':
    print(rri())


#  ██████ ██      ██████
# ██      ██      ██   ██
# ██      ██      ██   ██
# ██      ██      ██   ██
#  ██████ ███████ ██████


# cld = construct location directory
#
# rca = receiver cannal amount
# cdk = construct directory keys
# esl = encoder string length
#
# rlb = receiver location name


# define construct location directory
def cld(rca=8):

    # converts receiver channel amount to string length encoder
    esl = str(len(list(str(rca))) + 1)

    # construct identification string name
    cdk = "rlb_{:0" + esl + "d}"

    # construct location directory
    cld = dict(map(lambda x: (cdk.format(x), None), range(rca)))

    return cld


if __name__ == '__main__':
    print(cld())

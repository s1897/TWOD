
#  ██████ ██████  ██████
# ██      ██   ██ ██   ██
# ██      ██   ██ ██   ██
# ██      ██   ██ ██   ██
#  ██████ ██████  ██████


# cdd = construct distance directory
#
# poa = pwm output amount
# cdk = construct directory keys
# esl = encoder string length
#
# odn = output distance name


# define construct pwm directory
def cdd(poa=6):

    # converts pwm output amount to string length encoder
    esl = str(len(list(str(poa))) + 1)

    # construct identification string name
    cdk = "odn_{:0" + esl + "d}"

    # construct distance directory
    cdd = dict(map(lambda x: (cdk.format(x), {"x": None, "y": None}), range(poa)))

    return cdd


if __name__ == '__main__':
    print(cdd())

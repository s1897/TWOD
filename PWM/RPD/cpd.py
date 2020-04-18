
#  ██████ ██████  ██████
# ██      ██   ██ ██   ██
# ██      ██████  ██   ██
# ██      ██      ██   ██
#  ██████ ██      ██████


# cpd = construct pwm directory
#
# poa = pwm output amount
# cdk = construct directory keys
# esl = encoder string length
#
# opn = output pwm name


# define construct pwm directory
def cpd(poa=6):

    # converts pwm output amount to string length encoder
    esl = str(len(list(str(poa))) + 1)

    # construct identification string name
    cdk = "opn_{:0" + esl + "d}"

    # construct pwm directory
    cpd = dict(map(lambda x: (cdk.format(x), {"+x": None, "-x": None, "+y": None, "-y": None, "+c": None, "-c": None}), range(poa)))

    return cpd


if __name__ == '__main__':
    print(cpd())

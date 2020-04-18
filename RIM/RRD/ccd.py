
#  ██████  ██████ ██████
# ██      ██      ██   ██
# ██      ██      ██   ██
# ██      ██      ██   ██
#  ██████  ██████ ██████


# ccd = construct channel directory
#
# rca = receiver channel amount
# cdk = construct directory keys
# esl = encoder string length
#
# rcn = receiver channel name


# define construct channel directory
def ccd(rca=8):

    # converts receiver channel amount to string length encoder
    esl = str(len(list(str(rca))) + 1)

    # construct identification string name
    cdk = "rcn_{:0" + esl + "d}"

    # construct channel directory
    ccd = dict(map(lambda x: (cdk.format(x), None), range(rca)))

    return ccd


if __name__ == '__main__':
    print(ccd())

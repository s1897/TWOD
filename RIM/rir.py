
# ██████  ██ ██████
# ██   ██ ██ ██   ██
# ██████  ██ ██████
# ██   ██ ██ ██   ██
# ██   ██ ██ ██   ██

# rir = raw imput receiver
#
# rie = receiver imput encoder
# rid = register imput directory
# rin = receiver imput name
#
#

# import of required directories
# from RIM.rie import rie
from rie import rie

# define read receiver imput


def rir(rid):

    # trys to open the raw imput resiver files
    while True:
        try:
            # reads all pre-defined files and saves all data in a directory
            for rin in rid:
                rid[rin] = rie(int(open("/sys/kernel/rcio/rcin/ch{}".format(int(rin.split("_")[-1])), "r").read()[:-1]))

        except:
            # file could not be opened, so it will be tried again
            continue

        else:
            # file could be opened, this ended the try loop
            break

    # returns the register imput directory
    return rid


if __name__ == '__main__':
    rid = {'rin_00': None, 'rin_01': None, 'rin_02': None, 'rin_03': None, 'rin_04': None, 'rin_05': None, 'rin_06': None, 'rin_07': None}

    while True:
        print(rir({"tpn_02": None}))

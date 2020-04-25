
# ██████  ██ ██████
# ██   ██ ██ ██   ██
# ██████  ██ ██████
# ██   ██ ██ ██   ██
# ██   ██ ██ ██   ██

# rir = raw imput receiver
#
# rie = receiver imput encoder
# gdn = get directory name
# pdi = position directory imput
# pkn = psoition key name
# sdi = set directory imput
#
#

# import of required directories
from RIM.rie import rie


def rir(sdi, pdi={'tpi_00': 0, 'tpi_01': 1, 'tpi_02': 2, 'tpi_03': 3, 'tpi_04': 4, 'tpi_05': 5, 'tpi_06': 6, 'tpi_07': 7}):

    # gets directorys key name
    gdn = list(iter(sdi))[0].split("_")[0]

    # trys to open the raw imput resiver files
    while True:
        try:
            # reads all pre-defined files and saves all data in the set directory imput
            for pkn in pdi:
                sdi[gdn + "_" + pkn.split("_")[-1]] = rie(int(open("/sys/kernel/rcio/rcin/ch{}".format(pdi[pkn]), "r").read()[:-1]))

        except:
            # file could not be opened, so it will be tried again
            continue

        else:
            # file could be opened, this ended the try loop
            break

    # returns the register imput directory
    return sdi


if __name__ == '__main__':
    pass

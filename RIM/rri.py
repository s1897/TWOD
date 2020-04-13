
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██   ██ ██   ██ ██

# rri = reads receiver input and converts it. the values ​​are then saved in a directory
#
# rpd = register psition directory
# rcd = register cannal directory
# rcn = receiver cannal name
# rie = receiver imput encoder
#
#

# import of required directories
from NA2.rcinput import RCInput
# from RIM.rie import rie
from rie import rie
from time import sleep


# define read receiver imput
def rri(rcd, rpd):

    # registration function reciver imput
    nri = RCInput()

    for rpn in rpd:
        rcd["rcn_" + rpn.split("_")[-1]] = rie(int(nri.read(int(rpd[rpn]))))

    return rcd


if __name__ == '__main__':

    rcd = {'rcn_00': None, 'rcn_01': None, 'rcn_02': None, 'rcn_03': None, 'rcn_04': None, 'rcn_05': None, 'rcn_06': None, 'rcn_07': None}
    rpd = {'rpn_00': 0, 'rpn_01': 1, 'rpn_02': 2, 'rpn_03': 3, 'rpn_04': 4, 'rpn_05': 5, 'rpn_06': 6, 'rpn_07': 7}

    while True:
        rcd = rri(rcd, rpd)
        print(rcd)
        sleep(0.1)

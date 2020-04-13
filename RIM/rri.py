
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██   ██ ██   ██ ██

# rri = reads receiver input and converts it. the values ​​are then saved in a directory
#
#
# rie = receiver imput encoder
# rrc = register receiver channels
# rpd = register psition directory
# rpn = receiver psition name
# rcd = register cannal directory
# rcn = receiver cannal name
# nri = navio2 receiver imput
#
#

# import of required directories
from NA2.rcinput import RCInput
from NA2.util import check_apm
from RIM.rie import rie
from RIM.rrc import rrc


# define read receiver imput
def rri(rcd, rpd):

    # registration function reciver imput
    nri = RCInput()

    # puts the register psition directory together
    while True:

        # puts the convertet receiver imput into the receiver channel directory
        for rcn in rcd:
            rcd[rcn] = rie(int(nri.read(int(rcn.split("_")[-1]))))

        print(rcd)

# check_apm()
# rcin = RCInput()
# def rri(rc_cn):
#     return rie(float(rcin.read(rc_channl)))


if __name__ == '__main__':
    rcd = {'rcn_00': None, 'rcn_01': None, 'rcn_02': None, 'rcn_03': None, 'rcn_04': None, 'rcn_05': None, 'rcn_06': None, 'rcn_07': None}
    rpd = {'rpn_00': None, 'rpn_01': None, 'rpn_02': None, 'rpn_03': None, 'rpn_04': None, 'rpn_05': None, 'rpn_06': None, 'rpn_07': None}
    rri(rcd, rpd)

    # construct temporary positions directory
    # tpd = temporary positions directory
    # tpn = temporary positions name
    # tpd = {}
    # for tpn in rcd:
    #     tpd["tpd_" + tpn.split("_")[-1]] = int(tpn.split("_")[-1])

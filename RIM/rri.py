
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
from RIM.rie import rie


# define read receiver imput
def rri(rcd, rpd):

    # registration function reciver imput
    nri = RCInput()

    for rcn in rcd:
        rcd[rcn] = rie(int(nri.read(int(rcn.split("_")[-1]))))

    # for rpn in rpd:
    #     rcd["rcn_" + rpn.split("_")[-1]] = rie(int(nri.read(int(rpd[rpn]))))

    return rcd

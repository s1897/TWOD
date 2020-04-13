
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██   ██ ██   ██ ██

# rri = reads receiver input and converts it. the values ​​are then saved in a directory
# rpd = register psition directory
# rcd = register cannal directory
# rcn = receiver cannal name
#


# import of required directories
from NA2.rcinput import RCInput


# define read receiver imput
def rri(rcd, rpd):

    # registration function reciver imput
    nri = RCInput()

    for rpn in rpd:
        rcd["rcn_" + tpn.split("_")[-1]] = rie(int(nri.read(int(rpd[rpn]))))

    return rcd


#  ██████   █████  ██████
# ██    ██ ██   ██ ██   ██
# ██    ██ ███████ ██████
# ██ ▄▄ ██ ██   ██ ██   ██
#  ██████  ██   ██ ██   ██
#     ▀▀

# qar = quaternions and rotations
#
# xap = x axis psoition
# yap = y axis psoition
# zap = y axis psoition

# xyp = xy plane
# xzp = xz plane
# yzp = yz plane

# | +x  | -x  | +y  | -y  | +z  | -z  |
# |  f  |  g  |  h  |  j  |  k  |  l  |

# fhk = +x+y+z cube
# fhl = +x+y-z cube
# fjk = +x-y+z cube
# fjl = +x-y-z cube
# ghk = -x+y+z cube
# ghl = -x+y-z cube
# gjk = -x-y+z cube
# gjl = -x-y-z cube

# nsv = normalizd sensor vectord
# sod = sensor offset directory
# sdd = sensor data directory

# import of required directories
from IMU.CSD.rsd import rsd


def qar():

    nsv = 0
    sdd = rsd()

    for ml in sdd:
        for agm in sdd[ml]:
            for xyz in sdd[ml][agm]:
                nsv += sdd[ml][agm][xyz] * sdd[ml][agm][xyz]

            nsv **= 0.5

            for xyz in sdd[ml][agm]:
                sdd[ml][agm][xyz] /= nsv

    print(sdd)


if __name__ == '__main__':
    pass

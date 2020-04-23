
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

    print(
        "mpu9250: acc: x: {:+4f} y: {:+4f} z: {:+4f} gyr: x: {:+4f} y: {:+4f} z: {:+4f} mag: x: {:+4f} y: {:+4f} z {:+4f}  \n".format(
            sdd["mpu9250"]["acc"]["x"], sdd["mpu9250"]["acc"]["y"], sdd["mpu9250"]["acc"]["z"], sdd["mpu9250"]["gyr"]["x"], sdd["mpu9250"]["gyr"]["y"], sdd["mpu9250"]["gyr"]["z"], sdd["mpu9250"]["mag"]["x"], sdd["mpu9250"]["mag"]["y"], sdd["mpu9250"]["mag"]["z"]
        ) +
        "lsm9ds1: acc: x: {:+4f} y: {:+4f} z: {:+4f} gyr: x: {:+4f} y: {:+4f} z: {:+4f} mag: x: {:+4f} y: {:+4f} z {:+4f}  ".format(
            sdd["lsm9ds1"]["acc"]["x"], sdd["lsm9ds1"]["acc"]["y"], sdd["lsm9ds1"]["acc"]["z"], sdd["lsm9ds1"]["gyr"]["x"], sdd["lsm9ds1"]["gyr"]["y"], sdd["lsm9ds1"]["gyr"]["z"], sdd["lsm9ds1"]["mag"]["x"], sdd["lsm9ds1"]["mag"]["y"], sdd["lsm9ds1"]["mag"]["z"]
        ))


if __name__ == '__main__':
    pass

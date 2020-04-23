
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
# sdd = sensor data directory

# import of required directories
from IMU.CSD.rsd import rsd


def qar():

    sdd = rsd()

    print(("mpu9250: acc: {:+6f} {:+6f} {:+6f} gyr: {:+6f} {:+6f} {:+6f} mag: {:+6f} {:+6f} {:+6f}\n".format(sdd["mpu9250"]["acc"]["x"], sdd["mpu9250"]["acc"]["y"], sdd["mpu9250"]["acc"]["z"], sdd["mpu9250"]["gyr"]["x"], sdd["mpu9250"]["gyr"]["x"], sdd["mpu9250"]["gyr"]["x"], sdd["mpu9250"]["mag"]["x"], sdd["mpu9250"]["mag"]["x"], sdd["mpu9250"]["mag"]["x"]) +
           "lsm9ds1: acc: {:+6f} {:+6f} {:+6f} gyr: {:+6f} {:+6f} {:+6f} mag: {:+6f} {:+6f} {:+6f}".format(sdd["lsm9ds1"]["acc"]["x"], sdd["lsm9ds1"]["acc"]["y"], sdd["lsm9ds1"]["acc"]["z"], sdd["lsm9ds1"]["gyr"]["x"], sdd["lsm9ds1"]["gyr"]["x"], sdd["lsm9ds1"]["gyr"]["x"], sdd["lsm9ds1"]["mag"]["x"], sdd["lsm9ds1"]["mag"]["x"], sdd["lsm9ds1"]["mag"]["x"])))

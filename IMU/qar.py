
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

# cso = calculate sensor offset
# nsv = normalizd sensor vectord

# lsm = LSM9DS1
# mpu = MPU9250

# al = acc LSM9DS1
# gl = gyr LSM9DS1
# ml = mag LSM9DS1
# am = acc MPU9250
# gm = gyr MPU9250
# mm = mag MPU9250


# import of required directories
from NA2.lsm9ds1 import LSM9DS1
from NA2.mpu9250 import MPU9250

# set LSM9DS1 and MPU9250 sensor to a variable
lsm = LSM9DS1()
mpu = MPU9250()

# initialize the LSM9DS1 and MPU9250 sensor
lsm.initialize()
mpu.initialize()

while True:

    # read and write the data of the LSM9DS1 and MPU9250 sensor to a variable
    al, gl, ml = lsm.getMotion9()
    am, gm, mm = mpu.getMotion9()

    print(("Acc:" + " {:+6f} {:+6f} {:+6f} " + "Gyr:" + " {:+6f} {:+6f} {:+6f} " + "Mag:" + " {:+6f} {:+6f} {:+6f}").format(
        al[0], al[1], al[2], gl[0], gl[1], gl[2], ml[0], ml[1], ml[2]))
    print(("Acc:" + " {:+6f} {:+6f} {:+6f} " + "Gyr:" + " {:+6f} {:+6f} {:+6f} " + "Mag:" + " {:+6f} {:+6f} {:+6f}").format(
        am[0], am[1], am[2], gm[0], gm[1], gm[2], mm[0], mm[1], mm[2]))

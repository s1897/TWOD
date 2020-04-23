
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

# lms = LSM9DS1
# mpu = MPU9250

# import of required directories
from NA2.lsm9ds1 import LSM9DS1
from NA2.mpu9250 import MPU9250

# set LSM9DS1 and MPU9250 sensor to a variable
lms = LSM9DS1()
mpu = MPU9250()

# initialize the LSM9DS1 and MPU9250 sensor
lms.initialize()
mpu.initialize()

# read and write the data of the LSM9DS1 and MPU9250 sensor to a variable

gld = lms.getMotion9()  # 00 = ax, 01 = ay, 02 = az, 10 = gx, 11 = gy, 12 = gz, 20 = mx, 21 = my, 22 = mz
gmd = mpu.getMotion9()  # 00 = ax, 01 = ay, 02 = az, 10 = gx, 11 = gy, 12 = gz, 20 = mx, 21 = my, 22 = mz

print()
print(("lsm " + "Acc:" + " {:+6f} {:+6f} {:+6f} " + "Gyr:" + " {:+6f} {:+6f} {:+6f} " + "Mag:" + " {:+6f} {:+6f} {:+6f}").format(
    gld[0][0], gld[0][1], gld[0][2], gld[1][0], gld[1][1], gld[1][2], gld[2][0], gld[2][1], gld[2][2]))

print(("mpu " + "Acc:" + " {:+6f} {:+6f} {:+6f} " + "Gyr:" + " {:+6f} {:+6f} {:+6f} " + "Mag:" + " {:+6f} {:+6f} {:+6f}").format(
    gmd[0][0], gmd[0][1], gmd[0][2], gmd[1][0], gmd[1][1], gmd[1][2], gmd[2][0], gmd[2][1], gmd[2][2]))

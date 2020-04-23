
# ██████  ███████ ██████
# ██   ██ ██      ██   ██
# ██████  ███████ ██   ██
# ██   ██      ██ ██   ██
# ██   ██ ███████ ██████

# rsd = read sensor data

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


def rsd():
    # read and write the data of the LSM9DS1 and MPU9250 sensor to a variable
    al, gl, ml = lsm.getMotion9()
    am, gm, mm = mpu.getMotion9()

    d = {"mpu9250": {"acc": {"x": al[0], "y": al[1], "z": al[2]},
                     "gyr": {"x": gl[0], "y": gl[1], "z": gl[2]},
                     "mag": {"x": ml[0], "y": ml[1], "z": ml[2]}
                     },
         "lsm9ds1": {"acc": {"x": am[0], "y": am[1], "z": am[2]},
                     "gyr": {"x": gm[0], "y": gm[1], "z": gm[2]},
                     "mag": {"x": mm[0], "y": mm[1], "z": mm[2]}
                     }
         }

    return d

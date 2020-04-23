
# ███████  ██████  ██████
# ██      ██    ██ ██   ██
# ███████ ██    ██ ██   ██
#      ██ ██    ██ ██   ██
# ███████  ██████  ██████

# sod = sensor offset directory
#
#
# tod = temp offset directory
# sdd = sensor data directory
# sci = sensor calibration interval

# import of required directories
from IMU.CSD.rsd import rsd


def sod(sci=100):

    sod = {"mpu9250": {"acc": {"x": 0, "y": 0, "z": 0},
                       "gyr": {"x": 0, "y": 0, "z": 0},
                       "mag": {"x": 0, "y": 0, "z": 0}
                       },
           "lsm9ds1": {"acc": {"x": 0, "y": 0, "z": 0},
                       "gyr": {"x": 0, "y": 0, "z": 0},
                       "mag": {"x": 0, "y": 0, "z": 0}
                       }}

    tod = {"mpu9250": {"acc": {"x": 0, "y": 0, "z": 9.80665},
                       "gyr": {"x": 0, "y": 0, "z": 0},
                       "mag": {"x": 0, "y": 0, "z": 0}
                       },
           "lsm9ds1": {"acc": {"x": 0, "y": 0, "z": 9.80665},
                       "gyr": {"x": 0, "y": 0, "z": 0},
                       "mag": {"x": 0, "y": 0, "z": 0}
                       }}

    for i in range(sci):

        ssd = rsd()

        for ml in sod:
            for agm in sod[ml]:
                for xyz in sod[ml][agm]:
                    sod[ml][agm][xyz] += (ssd[ml][agm][xyz] / sci) - tod[ml][agm][xyz] / sci

    return(sod)


if __name__ == '__main__':
    sod()

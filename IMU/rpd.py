
# ██████  ██████  ██████
# ██   ██ ██   ██ ██   ██
# ██████  ██████  ██   ██
# ██   ██ ██      ██   ██
# ██   ██ ██      ██████


# rpd = rotation position directory
#
# xap = x axis psoition
# yap = y axis psoition
# zap = y axis psoition

# xyp = xy plane
# xzp = xz plane
# yzp = yz plane

# | +x  | -x  | +y  | -y  | +z  | -z  |
# |  f  |  g  |  h  |  j  |  k  |  l  |

# csn = cube sector name
#
# fhk = +x+y+z cube
# fhl = +x+y-z cube
# fjk = +x-y+z cube
# fjl = +x-y-z cube
# ghk = -x+y+z cube
# ghl = -x+y-z cube
# gjk = -x-y+z cube
# gjl = -x-y-z cube

# XY : +x+y  →  ±π×0  →  +π÷2  |  fhk  |  fhl  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
#      +y-x  →  +π÷2  →  ±π×1  |  ---  |  ---  |  ---  |  ---  |  ghk  |  ghl  |  ---  |  ---  |
#      +x-y  →  ±π×0  →  -π÷2  |  ---  |  ---  |  fjk  |  fjl  |  ---  |  ---  |  ---  |  ---  |
#      -y-x  →  -π÷2  →  ±π×1  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  gjk  |  gjl  |
#
# XZ : +x+z  →  ±π×0  →  +π÷2  |  fhk  |  ---  |  fjk  |  ---  |  ---  |  ---  |  ---  |  ---  |
#      +z-x  →  +π÷2  →  ±π×1  |  ---  |  ---  |  ---  |  ---  |  ghk  |  ---  |  gjk  |  ---  |
#      +x-z  →  ±π×0  →  -π÷2  |  ---  |  fhl  |  ---  |  fjl  |  ---  |  ---  |  ---  |  ---  |
#      -z-x  →  -π÷2  →  ±π×1  |  ---  |  ---  |  ---  |  ---  |  ---  |  ghl  |  ---  |  gjl  |
#
# YZ : +y+z  →  ±π×0  →  +π÷2  |  fhk  |  ---  |  ---  |  ---  |  ghk  |  ---  |  ---  |  ---  |
#      +z-y  →  +π÷2  →  ±π×1  |  ---  |  ---  |  fjk  |  ---  |  ---  |  ---  |  gjk  |  ---  |
#      +y-z  →  ±π×0  →  -π÷2  |  ---  |  fhl  |  ---  |  ---  |  ---  |  ghl  |  ---  |  ---  |
#      -z-y  →  -π÷2  →  ±π×1  |  ---  |  ---  |  ---  |  fjl  |  ---  |  ---  |  ---  |  gjl  |

# nsv = normalizd sensor vectord
# sod = sensor offset directory
# sdd = sensor data directory
# rsd = read sensor directory

# import of required directories
from IMU.CSD.rsd import rsd
from math import pi, atan


# define rotation position directory
def rpd():

    # set variables
    nsv = 0
    sdd = rsd()

    csn = {"mpu9250": None, "lsm9ds1": None}
    res = {"XY": None, "XZ": None, "YZ": None}

    # calculate te normaliz value
    for ml in sdd:
        for agm in sdd[ml]:
            for xyz in sdd[ml][agm]:

                nsv += sdd[ml][agm][xyz] * sdd[ml][agm][xyz]

            nsv **= 0.5

            # divide the sensor data directory whit the normalizd value
            for xyz in sdd[ml][agm]:
                sdd[ml][agm][xyz] /= nsv

    # difine the psoition cube
    for ml in sdd:

        # fhk = +x+y+z cube
        if sdd[ml]["acc"]["x"] > 0 and sdd[ml]["acc"]["y"] > 0 and sdd[ml]["acc"]["z"] > 0:
            csn[ml] = "fhk"

        # fhl = +x+y-z cube
        elif sdd[ml]["acc"]["x"] > 0 and sdd[ml]["acc"]["y"] > 0 and sdd[ml]["acc"]["z"] < 0:
            csn[ml] = "fhl"

        # fjk = +x-y+z cube
        elif sdd[ml]["acc"]["x"] > 0 and sdd[ml]["acc"]["y"] < 0 and sdd[ml]["acc"]["z"] > 0:
            csn[ml] = "fjk"

        # fjl = +x-y-z cube
        elif sdd[ml]["acc"]["x"] > 0 and sdd[ml]["acc"]["y"] < 0 and sdd[ml]["acc"]["z"] < 0:
            csn[ml] = "fjl"

        # ghk = -x+y+z cube
        elif sdd[ml]["acc"]["x"] < 0 and sdd[ml]["acc"]["y"] > 0 and sdd[ml]["acc"]["z"] > 0:
            csn[ml] = "ghk"

        # ghl = -x+y-z cube
        elif sdd[ml]["acc"]["x"] < 0 and sdd[ml]["acc"]["y"] > 0 and sdd[ml]["acc"]["z"] < 0:
            csn[ml] = "ghl"

        # gjk = -x-y+z cube
        elif sdd[ml]["acc"]["x"] < 0 and sdd[ml]["acc"]["y"] < 0 and sdd[ml]["acc"]["z"] > 0:
            csn[ml] = "gjk"

        # gjl = -x-y-z cube
        elif sdd[ml]["acc"]["x"] < 0 and sdd[ml]["acc"]["y"] < 0 and sdd[ml]["acc"]["z"] < 0:
            csn[ml] = "gjl"

    # abs all te values of the sensor data directory
    for ml in sdd:
        for agm in sdd[ml]:
            for xyz in sdd[ml][agm]:
                sdd[ml][agm][xyz] = abs(sdd[ml][agm][xyz])

    for ml in sdd:
        if csn[ml] == "fhk":
            # XY → +1 × ( atan ( y ÷ x ) ------- ) = αxy
            res["XY"] = +1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            # XZ → +1 × ( atan ( z ÷ x ) ------- ) = αxz
            res["XZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            # YZ → +1 × ( atan ( z ÷ y ) ------- ) = αyz
            res["YZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        elif csn[ml] == "fhl":
            # XY → +1 × ( atan ( y ÷ x ) ------- ) = αxy
            res["XY"] = +1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            # XZ → -1 × ( atan ( z ÷ x ) ------- ) = αxz
            res["XZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            # YZ → -1 × ( atan ( z ÷ y ) ------- ) = αyz
            res["YZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        elif csn[ml] == "fjk":
            # XY → -1 × ( atan ( y ÷ x ) ------- ) = αxy
            res["XY"] = -1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            # XZ → +1 × ( atan ( z ÷ x ) ------- ) = αxz
            res["XZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            # YZ → +1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res["YZ"] = +1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

        elif csn[ml] == "fjl":
            # XY → -1 × ( atan ( y ÷ x ) ------- ) = αxy
            res["XY"] = -1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            # XZ → -1 × ( atan ( z ÷ x ) ------- ) = αxz
            res["XZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            # YZ → -1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res["YZ"] = -1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

        elif csn[ml] == "ghk":
            # XY → +1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res["XY"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            # XZ → +1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res["XZ"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            # YZ → +1 × ( atan ( z - y ) ------- ) = αyz
            res["YZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        elif csn[ml] == "ghl":
            # XY → +1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res["XY"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            # XZ → -1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res["XZ"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            # YZ → -1 × ( atan ( z - y ) ------- ) = αyz
            res["YZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        elif csn[ml] == "gjk":
            # XY → -1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res["XY"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            # XZ → +1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res["XZ"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            # YZ → +1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res["YZ"] = +1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

        elif csn[ml] == "gjl":
            # XY → -1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res["XY"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            # XZ → -1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res["XZ"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            # YZ → -1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res["YZ"] = -1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

    print("XY: {:+4f} XZ: {:+4f} YZ: {:+4f}".format(res["XY"], res["XZ"], res["YZ"]))
    # print(
    #     "mpu9250: acc: x: {:+4f} y: {:+4f} z: {:+4f} gyr: x: {:+4f} y: {:+4f} z: {:+4f} mag: x: {:+4f} y: {:+4f} z {:+4f}  \n".format(
    #         sdd["mpu9250"]["acc"]["x"], sdd["mpu9250"]["acc"]["y"], sdd["mpu9250"]["acc"]["z"], sdd["mpu9250"]["gyr"]["x"], sdd["mpu9250"]["gyr"]["y"], sdd["mpu9250"]["gyr"]["z"], sdd["mpu9250"]["mag"]["x"], sdd["mpu9250"]["mag"]["y"], sdd["mpu9250"]["mag"]["z"]
    #     ) +
    #     "lsm9ds1: acc: x: {:+4f} y: {:+4f} z: {:+4f} gyr: x: {:+4f} y: {:+4f} z: {:+4f} mag: x: {:+4f} y: {:+4f} z {:+4f}  ".format(
    #         sdd["lsm9ds1"]["acc"]["x"], sdd["lsm9ds1"]["acc"]["y"], sdd["lsm9ds1"]["acc"]["z"], sdd["lsm9ds1"]["gyr"]["x"], sdd["lsm9ds1"]["gyr"]["y"], sdd["lsm9ds1"]["gyr"]["z"], sdd["lsm9ds1"]["mag"]["x"], sdd["lsm9ds1"]["mag"]["y"], sdd["lsm9ds1"]["mag"]["z"]
    #     ))
    #
    # print(csn)


if __name__ == '__main__':
    pass

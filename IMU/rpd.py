
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
# fh = +x+y plane
# gh = -x+y plane
# fj = +x-y plane
# gj = -x-y plane
#
# fk = +x+z plane
# gk = -x+z plane
# fl = +x-z plane
# gl = -x-z plane
#
# hk = +y+z plane
# jk = -y+z plane
# hl = +y-z plane
# jl = -y-z plane
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
from math import pi, atan, degrees


# define rotation position directory
def rpd():

    # set variables
    nsv = 0
    sdd = rsd()

    csn = {"mpu9250": None, "lsm9ds1": None}
    res = {"mpu9250": {"XY": None, "XZ": None, "YZ": None}, "lsm9ds1": {"XY": None, "XZ": None, "YZ": None}}

    # calculate te normaliz value
    for ml in sdd:
        for agm in sdd[ml]:
            for xyz in sdd[ml][agm]:

                nsv += sdd[ml][agm][xyz] * sdd[ml][agm][xyz]

            nsv **= 0.5

            # divide the sensor data directory whit the normalizd value
            for xyz in sdd[ml][agm]:
                sdd[ml][agm][xyz] /= nsv

    # difine the psoition cube and plane
    for ml in sdd:

        # fh = +x+y plane
        if sdd[ml]["acc"]["x"] > 0 and sdd[ml]["acc"]["y"] > 0 and sdd[ml]["acc"]["z"] == 0:
            csn[ml] = "fh"

        # gh = -x+y plane
        elif sdd[ml]["acc"]["x"] < 0 and sdd[ml]["acc"]["y"] > 0 and sdd[ml]["acc"]["z"] == 0:
            csn[ml] = "gh"

        # fj = +x-y plane
        elif sdd[ml]["acc"]["x"] > 0 and sdd[ml]["acc"]["y"] < 0 and sdd[ml]["acc"]["z"] == 0:
            csn[ml] = "fj"

        # gj = -x-y plane
        elif sdd[ml]["acc"]["x"] < 0 and sdd[ml]["acc"]["y"] < 0 and sdd[ml]["acc"]["z"] == 0:
            csn[ml] = "gj"

        # fk = +x+z plane
        elif sdd[ml]["acc"]["x"] > 0 and sdd[ml]["acc"]["y"] == 0 and sdd[ml]["acc"]["z"] > 0:
            csn[ml] = "fk"

        # gk = -x+z plane
        elif sdd[ml]["acc"]["x"] < 0 and sdd[ml]["acc"]["y"] == 0 and sdd[ml]["acc"]["z"] > 0:
            csn[ml] = "gk"

        # fl = +x-z plane
        elif sdd[ml]["acc"]["x"] > 0 and sdd[ml]["acc"]["y"] == 0 and sdd[ml]["acc"]["z"] < 0:
            csn[ml] = "fl"

        # gl = -x-z plane
        elif sdd[ml]["acc"]["x"] < 0 and sdd[ml]["acc"]["y"] == 0 and sdd[ml]["acc"]["z"] < 0:
            csn[ml] = "gl"

        # hk = +y+z plane
        elif sdd[ml]["acc"]["x"] == 0 and sdd[ml]["acc"]["y"] > 0 and sdd[ml]["acc"]["z"] > 0:
            csn[ml] = "hk"

        # jk = -y+z plane
        elif sdd[ml]["acc"]["x"] == 0 and sdd[ml]["acc"]["y"] < 0 and sdd[ml]["acc"]["z"] > 0:
            csn[ml] = "jk"

        # hl = +y-z plane
        elif sdd[ml]["acc"]["x"] == 0 and sdd[ml]["acc"]["y"] > 0 and sdd[ml]["acc"]["z"] < 0:
            csn[ml] = "hl"

        # jl = -y-z plane
        elif sdd[ml]["acc"]["x"] == 0 and sdd[ml]["acc"]["y"] < 0 and sdd[ml]["acc"]["z"] < 0:
            csn[ml] = "jl"

        # fhk = +x+y+z cube
        elif sdd[ml]["acc"]["x"] > 0 and sdd[ml]["acc"]["y"] > 0 and sdd[ml]["acc"]["z"] > 0:
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
        # fh = +x+y plane
        if csn[ml] == "fh":
            # XY → +1 × ( atan ( y ÷ x ) ------- ) = αxy
            res[ml]["XY"] = +1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            res[ml]["XZ"] = 0

            res[ml]["YZ"] = 0

        # gh = -x+y plane
        elif csn[ml] == "gh":
            # XY → +1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res[ml]["XY"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            res[ml]["XZ"] = pi

            res[ml]["YZ"] = 0

        # fj = +x-y plane
        elif csn[ml] == "fj":
            # XY → -1 × ( atan ( y ÷ x ) ------- ) = αxy
            res[ml]["XY"] = -1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            res[ml]["XZ"] = 0

            res[ml]["YZ"] = pi

        # gj = -x-y plane
        elif csn[ml] == "gj":
            # XY → -1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res[ml]["XY"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            res[ml]["XZ"] = pi

            res[ml]["YZ"] = pi

        # fk = +x+z plane
        elif csn[ml] == "fk":
            res[ml]["XY"] = 0

            # XZ → +1 × ( atan ( z ÷ x ) ------- ) = αxz
            res[ml]["XZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            res[ml]["YZ"] = pi / 2

        # gk = -x+z plane
        elif csn[ml] == "gk":
            res[ml]["XY"] = pi

            # XZ → +1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res[ml]["XZ"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            res[ml]["YZ"] = pi / 2

        # fl = +x-z plane
        elif csn[ml] == "fl":
            res[ml]["XY"] = 0

            # XZ → -1 × ( atan ( z ÷ x ) ------- ) = αxz
            res[ml]["XZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            res[ml]["YZ"] = -pi / 2

        # gl = -x-z plane
        elif csn[ml] == "gl":
            res[ml]["XY"] = pi

            # XZ → -1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res[ml]["XZ"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            res[ml]["YZ"] = -pi / 2

        # hk = +y+z plane
        elif csn[ml] == "hk":
            res[ml]["XY"] = pi / 2

            res[ml]["XZ"] = pi / 2

            # YZ → +1 × ( atan ( z ÷ y ) ------- ) = αyz
            res[ml]["YZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        # jk = -y+z plane
        elif csn[ml] == "jk":
            res[ml]["XY"] = -pi / 2

            res[ml]["XZ"] = pi / 2

            # YZ → +1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res[ml]["YZ"] = +1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

        # hl = +y-z plane
        elif csn[ml] == "hl":
            res[ml]["XY"] = pi / 2

            res[ml]["XZ"] = -pi / 2

            # YZ → -1 × ( atan ( z ÷ y ) ------- ) = αyz
            res[ml]["YZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        # jl = -y-z plane
        elif csn[ml] == "jl":
            res[ml]["XY"] = -pi / 2

            res[ml]["XZ"] = -pi / 2

            # YZ → -1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res[ml]["YZ"] = -1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

        if csn[ml] == "fhk":
            # XY → +1 × ( atan ( y ÷ x ) ------- ) = αxy
            res[ml]["XY"] = +1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            # XZ → +1 × ( atan ( z ÷ x ) ------- ) = αxz
            res[ml]["XZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            # YZ → +1 × ( atan ( z ÷ y ) ------- ) = αyz
            res[ml]["YZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        elif csn[ml] == "fhl":
            # XY → +1 × ( atan ( y ÷ x ) ------- ) = αxy
            res[ml]["XY"] = +1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            # XZ → -1 × ( atan ( z ÷ x ) ------- ) = αxz
            res[ml]["XZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            # YZ → -1 × ( atan ( z ÷ y ) ------- ) = αyz
            res[ml]["YZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        elif csn[ml] == "fjk":
            # XY → -1 × ( atan ( y ÷ x ) ------- ) = αxy
            res[ml]["XY"] = -1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            # XZ → +1 × ( atan ( z ÷ x ) ------- ) = αxz
            res[ml]["XZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            # YZ → +1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res[ml]["YZ"] = +1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

        elif csn[ml] == "fjl":
            # XY → -1 × ( atan ( y ÷ x ) ------- ) = αxy
            res[ml]["XY"] = -1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            # XZ → -1 × ( atan ( z ÷ x ) ------- ) = αxz
            res[ml]["XZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            # YZ → -1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res[ml]["YZ"] = -1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

        elif csn[ml] == "ghk":
            # XY → +1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res[ml]["XY"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            # XZ → +1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res[ml]["XZ"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            # YZ → +1 × ( atan ( z - y ) ------- ) = αyz
            res[ml]["YZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        elif csn[ml] == "ghl":
            # XY → +1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res[ml]["XY"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            # XZ → -1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res[ml]["XZ"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            # YZ → -1 × ( atan ( z - y ) ------- ) = αyz
            res[ml]["YZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        elif csn[ml] == "gjk":
            # XY → -1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res[ml]["XY"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            # XZ → +1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res[ml]["XZ"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            # YZ → +1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res[ml]["YZ"] = +1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

        elif csn[ml] == "gjl":
            # XY → -1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res[ml]["XY"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            # XZ → -1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res[ml]["XZ"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            # YZ → -1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res[ml]["YZ"] = -1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

    print("mpu9250: XY: {:+4f} XZ: {:+4f} YZ: {:+4f} lsm9ds1: XY: {:+4f} XZ: {:+4f} YZ: {:+4f}".format(degrees(res["mpu9250"]["XY"]), degrees(res["mpu9250"]["XZ"]), degrees(res["mpu9250"]["YZ"]), degrees(res["lsm9ds1"]["XY"]), degrees(res["lsm9ds1"]["XZ"]), degrees(res["lsm9ds1"]["YZ"]))))

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

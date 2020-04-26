
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
            res["XY"] = +1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            res["XZ"] = 0

            res["YZ"] = 0

        # gh = -x+y plane
        elif csn[ml] == "gh":
            # XY → +1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res["XY"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            res["XZ"] = pi

            res["YZ"] = 0

        # fj = +x-y plane
        elif csn[ml] == "fj":
            # XY → -1 × ( atan ( y ÷ x ) ------- ) = αxy
            res["XY"] = -1 * atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["x"])

            res["XZ"] = 0

            res["YZ"] = pi

        # gj = -x-y plane
        elif csn[ml] == "gj":
            # XY → -1 × ( atan ( x ÷ y ) + π ÷ 2 ) = αxy
            res["XY"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["y"]) + pi / 2)

            res["XZ"] = pi

            res["YZ"] = pi

        # fk = +x+z plane
        elif csn[ml] == "fk":
            res["XY"] = 0

            # XZ → +1 × ( atan ( z ÷ x ) ------- ) = αxz
            res["XZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            res["YZ"] = pi / 2

        # gk = -x+z plane
        elif csn[ml] == "gk":
            res["XY"] = pi

            # XZ → +1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res["XZ"] = +1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            res["YZ"] = pi / 2

        # fl = +x-z plane
        elif csn[ml] == "fl":
            res["XY"] = 0

            # XZ → -1 × ( atan ( z ÷ x ) ------- ) = αxz
            res["XZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["x"])

            res["YZ"] = -pi / 2

        # gl = -x-z plane
        elif csn[ml] == "gl":
            res["XY"] = pi

            # XZ → -1 × ( atan ( x ÷ z ) + π ÷ 2 ) = αxz
            res["XZ"] = -1 * (atan(sdd[ml]["acc"]["x"] / sdd[ml]["acc"]["z"]) + pi / 2)

            res["YZ"] = -pi / 2

        # hk = +y+z plane
        elif csn[ml] == "hk":
            res["XY"] = pi / 2

            res["XZ"] = pi / 2

            # YZ → +1 × ( atan ( z ÷ y ) ------- ) = αyz
            res["YZ"] = +1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        # jk = -y+z plane
        elif csn[ml] == "jk":
            res["XY"] = -pi / 2

            res["XZ"] = pi / 2

            # YZ → +1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res["YZ"] = +1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

        # hl = +y-z plane
        elif csn[ml] == "hl":
            res["XY"] = pi / 2

            res["XZ"] = -pi / 2

            # YZ → -1 × ( atan ( z ÷ y ) ------- ) = αyz
            res["YZ"] = -1 * atan(sdd[ml]["acc"]["z"] / sdd[ml]["acc"]["y"])

        # jl = -y-z plane
        elif csn[ml] == "jl":
            res["XY"] = -pi / 2

            res["XZ"] = -pi / 2

            # YZ → -1 × ( atan ( y ÷ z ) + π ÷ 2 ) = αyz
            res["YZ"] = -1 * (atan(sdd[ml]["acc"]["y"] / sdd[ml]["acc"]["z"]) + pi / 2)

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

    print("XY: {:+4f} XZ: {:+4f} YZ: {:+4f}".format(degrees(res["XY"]), degrees(res["XZ"]), degrees(res["YZ"])))

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

XY: -135.000000 XZ: -90.108721 YZ: -90.108721
XY: +64.536655 XZ: -89.731763 YZ: -89.436717
XY: +23.962489 XZ: -89.757451 YZ: -89.892200
XY: +14.743563 XZ: -89.486514 YZ: -89.864869
XY: -68.198591 XZ: -89.785310 YZ: -90.536713
XY: +69.443955 XZ: -89.919377 YZ: -89.785007
XY: +40.236358 XZ: -89.641906 YZ: -89.696996
XY: +126.869898 XZ: -90.243926 YZ: -89.674767
XY: +75.963757 XZ: -89.946652 YZ: -89.786609
XY: +63.434949 XZ: -89.731512 YZ: -89.463036
XY: -116.565051 XZ: -90.054053 YZ: -90.108105
XY: +16.990823 XZ: -89.033527 YZ: -89.704664
XY: +38.659808 XZ: -89.732390 YZ: -89.785911
XY: +0.000000 XZ: +0.000000 YZ: -89.671504
XY: +32.735226 XZ: -89.621637 YZ: -89.756765
XY: -12.094757 XZ: -89.627263 YZ: -90.079873
XY: +125.217593 XZ: -90.326004 YZ: -89.538166
XY: +49.085617 XZ: -89.645147 YZ: -89.590556
XY: +85.236358 XZ: -89.972807 YZ: -89.673687
XY: -29.357754 XZ: -89.573224 YZ: -90.240065
XY: +111.801409 XZ: -90.054053 YZ: -89.864869
XY: +115.201124 XZ: -90.218269 YZ: -89.536187
XY: +60.945396 XZ: -89.864099 YZ: -89.755380
XY: +66.801409 XZ: -89.918266 YZ: -89.809287
XY: +73.739795 XZ: -89.812321 YZ: -89.356555
XY: +79.215702 XZ: -89.891588 YZ: -89.430855
XY: -45.000000 XZ: -89.973151 YZ: -90.026849
XY: -82.234834 XZ: -89.918537 YZ: -90.597375
XY: +40.601295 XZ: -89.809196 YZ: -89.836454
XY: +72.474432 XZ: -89.838224 YZ: -89.487722
XY: +98.130102 XZ: -90.026724 YZ: -89.812934
XY: +54.462322 XZ: -89.861337 YZ: -89.805872
XY: +92.602562 XZ: -90.026849 YZ: -89.409343
XY: +59.036243 XZ: -89.837074 YZ: -89.728458
XY: +0.000000 XZ: -89.918460 YZ: +0.000000
XY: +50.710593 XZ: -89.754798 YZ: -89.700310
XY: +29.357754 XZ: -89.570223 YZ: -89.758247
XY: -52.125016 XZ: -89.810190 YZ: -90.244041
XY: -116.565051 XZ: -90.053976 YZ: -90.107952
XY: +26.565051 XZ: -89.891639 YZ: -89.945820
XY: +130.601295 XZ: -90.320682 YZ: -89.625872
XY: +23.198591 XZ: -89.810280 YZ: -89.918691
XY: +106.389540 XZ: -90.136094 YZ: -89.537289
XY: +111.801409 XZ: -90.108309 YZ: -89.729228
XY: +93.366461 XZ: -90.026975 YZ: -89.541428
XY: +50.194429 XZ: -89.865123 YZ: -89.838148
XY: -65.224859 XZ: -89.837613 YZ: -90.351836
XY: +70.346176 XZ: -89.863712 YZ: -89.618397
XY: +104.931417 XZ: -90.108156 YZ: -89.594421
XY: +23.962489 XZ: -89.759712 YZ: -89.893205
XY: +116.565051 XZ: -90.080736 YZ: -89.838528
XY: +125.217593 XZ: -90.320383 YZ: -89.546129
XY: +49.899092 XZ: -89.573422 YZ: -89.493443
XY: +66.037511 XZ: -89.890709 YZ: -89.754097
XY: +150.255119 XZ: -90.380878 YZ: -89.782353
XY: +69.443955 XZ: -89.837305 YZ: -89.566155
XY: +28.072487 XZ: -89.594229 YZ: -89.783586
XY: -105.255119 XZ: -90.080509 YZ: -90.295198
XY: +0.000000 XZ: +0.000000 YZ: -89.106096
XY: +140.194429 XZ: -90.163858 YZ: -89.863452
XY: -99.462322 XZ: -90.027026 YZ: -90.162157
XY: +97.594643 XZ: -90.053900 YZ: -89.595756
XY: +0.000000 XZ: -89.892604 YZ: +0.000000
XY: -168.690068 XZ: -90.133556 YZ: -90.026711
XY: +23.198591 XZ: -89.623943 YZ: -89.838831
XY: +17.525568 XZ: -89.491313 YZ: -89.839358

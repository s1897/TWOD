from NAVIO2.rcinput import *

# ---------- Initialise the RCInput() class ----------
imputRC = RCInput()

# ---------- Define the Receiver funktion ------------

chNum = 8


def rc_R_rcsqdb(rawReadDict=dict(map(lambda x: (("rawSi{:0" + str(len(list(str(chNum))) + 1) + "d}").format(x), x), range(chNum)))):

    rawRead = {}

    for rawSi in rawReadDict:

        rawRead[rawSi] = int(imputRC.read(rawReadDict[rawSi]))

    return rawRead


def rc_C_rcsqdb(rc_R_rcsqdb, rawConvDict=dict(map(lambda x: (("rawSi{:0" + str(len(list(str(chNum))) + 1) + "d}").format(x), {"lowRaw": -1, "highRaw": +1}), range(chNum))), lowRawIm=982, highRawIm=2006):

    rawConvOut = {}

    rawImDiff = highRawIm - lowRawIm

    for rawCo in rc_R_rcsqdb:

        rawDiff = rawConvDict[rawCo]["highRaw"] - rawConvDict[rawCo]["lowRaw"]

        rawConvOut[rawCo] = (rawDiff / rawImDiff) * (rc_R_rcsqdb[rawCo] - lowRawIm) + rawConvDict[rawCo]["lowRaw"]

    return rawConvOut


def rc_S_rcsqdb():

    setRawRC = dict(map(lambda x: (("rawSi{:0" + str(len(list(str(chNum))) + 1) + "d}").format(x), None), range(chNum)))

    rawPos = 0

    while True:

        rawDictRC = rc_C_rcsqdb(rc_R_rcsqdb())

        for rawRC in rawDictRC:

            if rawDictRC[rawRC] > 0.9 and setRawRC[rawRC] == None:

                while True:

                    rawDictRC = rc_C_rcsqdb(rc_R_rcsqdb())

                    if rawDictRC[rawRC] < -0.9:

                        setRawRC[rawRC] = rawPos

                        print(rawRC, rawPos)

                        rawPos += 1

                        break

        if rawPos > 7:
            break

    return setRawRC


if __name__ == '__main__':

    g = rc_S_rcsqdb()

    while True:
        print(rc_C_rcsqdb(rc_R_rcsqdb(g)))

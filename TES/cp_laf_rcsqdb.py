from math import *


def cp_L_rcsqdb(numEngin, typEngine="I", radEngine=500):
    abEngin = 360 / numEngin

    if typEngine == "I":
        saEngin = 0

    elif typEngine == "V":
        saEngin = abEngin / 2

    xAxis = dict(map(lambda x: (x, round(sin(radians(saEngin + (abEngin * x))) * radEngine, 12)), range(numEngin)))
    yAxis = dict(map(lambda x: (x, round(cos(radians(saEngin + (abEngin * x))) * radEngine, 12)), range(numEngin)))
    aDict = dict(map(lambda x: (x, saEngin + (abEngin * x)), range(numEngin)))

    return xAxis, yAxis, aDict


def cp_A_rcsqdb(xya):
    xAxis, yAxis, aDict = xya
    alEngine = {"+yAxis": {}, "-yAxis": {}, "+xAxis": {}, "-xAxis": {}}

    for e in aDict:

        if 0 < aDict[e] and aDict[e] <= 90 or 90 <= aDict[e] and aDict[e] < 180:
            alEngine["-xAxis"][e] = xAxis[e]

        if 90 < aDict[e] and aDict[e] <= 180 or 180 <= aDict[e] and aDict[e] < 270:
            alEngine["+yAxis"][e] = yAxis[e]

        if 180 < aDict[e] and aDict[e] <= 270 or 270 <= aDict[e] and aDict[e] < 360:
            alEngine["+xAxis"][e] = xAxis[e]

        if 270 < aDict[e] and aDict[e] <= 360 or 0 <= aDict[e] and aDict[e] < 90:
            alEngine["-yAxis"][e] = yAxis[e]

    return alEngine


def cp_F_rcsqdb(alEngine, radius=500):

    for axis in alEngine:

        for numE in alEngine[axis]:

            alEngine[axis][numE] = abs((radius / (alEngine[axis][numE])) / len(alEngine[axis]))

    return alEngine


if __name__ == '__main__':

    print(cp_F_rcsqdb(cp_A_rcsqdb(cp_L_rcsqdb(5, "I"))))

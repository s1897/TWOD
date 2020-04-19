
# ██████   ██████ ██████
# ██   ██ ██      ██   ██
# ██████  ██      ██   ██
# ██      ██      ██   ██
# ██       ██████ ██████

# pcd = pwm control distribution
#
# cdd = construct distance directory
# cpn = construct distance name
#
# cpd = construct pwm directory
# cpn = construct pwm name
#
# rci = raw control imput
#
# gdk = get distance key
# grk = get receiver key
from math import sqrt


def pcd(rci, cdd, cpd):

    gdk = list(iter(cdd))[0].split("_")[0]
    grk = list(iter(rci))[0].split("_")[0]

    t = {"y": rci["rcn_02"], "x": rci["rcn_03"]}

    for cpn in cpd:

        h = cdd[gdk + "_" + cpn.split("_")[-1]]
        cpd[cpn] = round(abs((h["x"] - t["x"] * (1 - ((t["y"] / 2))**0.5))**2 + (h["y"] - t["y"] * ((1 - (t["x"] / 2))**0.5))**2)**0.5, 12)

    return cpd


if __name__ == '__main__':

    cdd = {'odn_00': {'x': 0.0, 'y': 1.0}, 'odn_01': {'x': 0.951056516295, 'y': 0.309016994375}, 'odn_02': {'x': 0.587785252292, 'y': -0.809016994375},
           'odn_03': {'x': -0.587785252292, 'y': -0.809016994375}, 'odn_04': {'x': -0.951056516295, 'y': 0.309016994375}, 'odn_05': {'x': 0.0, 'y': -0.145326}}

    rci = {'rcn_00': None, 'rcn_01': None, 'rcn_02': 0, 'rcn_03': 0, 'rcn_04': None, 'rcn_05': None, 'rcn_06': None, 'rcn_07': None}

    cpd = {'opn_00': None, 'opn_01': None, 'opn_02': None, 'opn_03': None, 'opn_04': None, 'opn_05': None}

    print(pcd(rci, cdd, cpd))
# print(100 * ((0.0009419325139 - 0.0008182609046) * 0.006283185307) / ((0.0009512986886 - 0.0008182609046) * 0.006283185307))
# 92.9597634458493

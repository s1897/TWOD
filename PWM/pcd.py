
# ██████   ██████ ██████
# ██   ██ ██      ██   ██
# ██████  ██      ██   ██
# ██      ██      ██   ██
# ██       ██████ ██████

# pcd = pwm control distribution
#
# rir = raw imput receiver
# ppd = pwm psition distribution
#
# cpd = construct pwm directory
# cpn = construct pwm name
#
# gdk = get distance key
# grk = get receiver key
#

#
# thr = thrust
# rot = rotate
#
# ypr  = y position of receiver
# xpr  = x position of receiver
#
# ype  = y position of engine
# xpe  = x position of engine
#
#
from RIM.rie import rie


def pcd(rir, ppd, cpd):

    grk = list(iter(rir))[0].split("_")[0]
    gdk = list(iter(ppd))[0].split("_")[0]

    for rcn in rir:
        if rcn == grk + "_00":
            thr = rie(rir[grk + "_00"], elo=0, eho=1, lsr=-1, hsr=1)

        elif rcn == grk + "_01":
            rot = rir[grk + "_01"]

        elif rcn == grk + "_02":
            ypr = rir[grk + "_02"]

        elif rcn == grk + "_03":
            xpr = rir[grk + "_03"]
        else:
            break

    for cpn in cpd:
        ype = ppd[gdk + "_" + cpn.split("_")[-1]]["y"]
        xpe = ppd[gdk + "_" + cpn.split("_")[-1]]["x"]

        ypr *= (1 - (xpr**2 / 2))**0.5
        xpr *= (1 - (ypr**2 / 2))**0.5

        cpd[cpn] = round(thr + (((ype - ypr)**2 + (xpe - xpr)**2)**0.5 - 2) * 0.1, 12)

    return cpd


if __name__ == '__main__':

    ppd = {'odn_00': {'x': 0.0, 'y': 1.0}, 'odn_01': {'x': 0.951056516295, 'y': 0.309016994375}, 'odn_02': {'x': 0.587785252292, 'y': -0.809016994375},
           'odn_03': {'x': -0.587785252292, 'y': -0.809016994375}, 'odn_04': {'x': -0.951056516295, 'y': 0.309016994375}, 'odn_05': {'x': 0.0, 'y': -0.145326}}

    rir = {'rcn_00': 1, 'rcn_01': 2, 'rcn_02': 0, 'rcn_03': 0, 'rcn_04': None, 'rcn_05': None, 'rcn_06': None, 'rcn_07': None}

    cpd = {'opn_00': None, 'opn_01': None, 'opn_02': None, 'opn_03': None, 'opn_04': None, 'opn_05': None}

    print(pcd(rir, ppd, cpd))


# ██████  ██████  ██████
# ██   ██ ██   ██ ██   ██
# ██████  ██████  ██   ██
# ██      ██      ██   ██
# ██      ██      ██████

# ppd = pwm psition distribution
#
# sdi = set directory imput
# sdn = set directory name
#
# tes = thrust engine shape, code I ore X
# tea = thrust engine amount
# ter = thrust engine radius
# ted = thrust engine degrees
# teg = thrust engine gradient
# tec = thrust engine counter
#
# ees = equalizer engine shape, code I ore X
# eea = equalizer engine amount
# eer = equalizer engine radius
# eed = equalizer engine degrees
# eeg = equalizer engine gradient
# eec = equalizer engine counter
#

# import of required directories
from math import cos, sin, radians


# define pwm psition distribution
def ppd(sdi, tea=5, ter=500, tes="I", eea=1, eer=72.663, ees="X"):

    if len(sdi) != tea + eea:
        raise Exception("the amount of thrust engine amount + equalizer engine amount must be the same as pwm outputs")

    if tea > 0 or eea > 0:

        if tea > 0:

            teg = 360 / tea
            tec = 0

            if tes == "X":
                ted = (360 / tea) / 2
            elif tes == "I":
                ted = 0
            else:
                raise Exception("thrust engine shape code must be I or X")

        if eea > 0:

            eeg = 360 / eea
            eec = 0

            if ees == "X":
                eed = (360 / eea) / 2
            elif ees == "I":
                eed = 0
            else:
                raise Exception("equalizer engine shape must be I or X")

    else:
        raise Exception("thrust engine amount and equalizer engine amount can't be both zero")

    for sdn in sdi:
        if tea != tec:
            sdi[sdn][list(iter(sdi[sdn]))[0]] = round(1 / ter * (ter * sin(radians(ted + (teg * (tec))))), 12)
            sdi[sdn][list(iter(sdi[sdn]))[-1]] = round(1 / ter * (ter * cos(radians(ted + (teg * (tec))))), 12)

            tec += 1

        elif eea != eec:
            sdi[sdn][list(iter(sdi[sdn]))[0]] = round(1 / ter * (eer * sin(radians(eed + (eeg * (eec))))), 12)
            sdi[sdn][list(iter(sdi[sdn]))[-1]] = round(1 / ter * (eer * cos(radians(eed + (eeg * (eec))))), 12)

            eec += 1

    return sdi


if __name__ == '__main__':
    l = {'odn_00': {'x': None, 'y': None}, 'odn_01': {'x': None, 'y': None}, 'odn_02': {'x': None, 'y': None},
         'odn_03': {'x': None, 'y': None}, 'odn_04': {'x': None, 'y': None}, 'odn_05': {'x': None, 'y': None}}

    print(ppd(l))

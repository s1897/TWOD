
# ██ ██████   ██████
# ██ ██   ██ ██
# ██ ██████  ██
# ██ ██   ██ ██
# ██ ██   ██  ██████

# irc = initialize receiver control
#
# sdi = set directory imput
# sdn = set directory name
# rtd = read temporary directory
# rtn = read temporary name
# gdn = get directory name
# pcn = psition control nummer
# led = light emitting diode
#
#

# import of required directories
from NA2.leds import Led
from RIM.rir import rir


# define read receiver imput
def irc(sdi):

    # registration function reciver imput and leds
    led = Led()

    # gets directorys key name
    gdn = list(iter(sdi))[0].split("_")[0]

    # construct temporary positions directory
    rtd = {}
    for sdn in sdi:
        rtd["rtn_" + sdn.split("_")[-1]] = None

    # set psition control nummer
    pcn = 0

    # puts the register psition directory together
    while True:

        # converted and add receiver input to temporary positions directory and update them
        rtd = rir(rtd)

        # tests whether one of the values ​​comes from the temporary positions directory above 0.9 and
        # whether the register psition directory with the same number contains the value None.
        for rtn in rtd:
            if rtd[rtn] > 0.9 and sdi[gdn + "_" + rtn.split("_")[-1]] == None:

                # set led color to White
                led.setColor('White')

                while True:

                    # update the convertet receiver imput into the receiver channel directory
                    rtd[rtn] = rir({rtn: rtd[rtn]})[rtn]

                    # tests whether one of the values ​​comes from the temporary positions directory under -0.9 and
                    # whether the register psition directory with the same number contains the value None
                    if rtd[rtn] < -0.9 and sdi[gdn + "_" + rtn.split("_")[-1]] == None:

                        # set led color to Black
                        led.setColor('Black')

                        # set the position value in the register psition directory
                        sdi[gdn + "_" + rtn.split("_")[-1]] = pcn

                        # add one to psition control nummer and break the while loop
                        pcn += 1
                        break

        # tests for the value to be deleted and whether it has already been deleted
        for sdn in sdi:
            if sdi[sdn] != None and "rtn_" + sdn.split("_")[-1] in rtd:

                # deletes the previously tested value from the temporary positions directory.
                rtd.__delitem__("rtn_" + sdn.split("_")[-1])

        # the loop is interrupted when the temporary positions directory has no more value
        if rtd == dict():
            break

    # set led color to Green
    led.setColor('Green')

    # returns register psition directory
    return sdi


if __name__ == '__main__':
    print("")

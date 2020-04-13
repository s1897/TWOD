
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██████  ██████  ██
# ██   ██ ██   ██ ██
# ██   ██ ██   ██ ██

# rri = reads receiver input and converts it. the values ​​are then saved in a directory
#
#
# rie = receiver imput encoder
# rrc = register receiver channels
# rpd = register psition directory
# rpn = receiver psition name
# rcd = register cannal directory
# rcn = receiver cannal name
# tpd = temporary positions directory
# tpn = temporary positions name
# nri = navio2 receiver imput
# pcn = psition control nummer
# led = light emitting diode
#
#

# import of required directories
from NA2.rcinput import RCInput
from NA2.leds import Led
from RIM.rie import rie
from RIM.rrc import rrc


# define read receiver imput
def rri(rpd):

    # registration function reciver imput and leds
    nri = RCInput()
    led = Led()

    # construct temporary positions directory
    tpd = {}
    for tpn in rpd:
        tpd["tpn_" + tpn.split("_")[-1]] = None

    # set psition control nummer
    pcn = 0

    # puts the register psition directory together
    while True:

        # converted and add receiver input to temporary positions directory and update them
        for tpn in tpd:
            tpd[tpn] = rie(int(nri.read(int(tpn.split("_")[-1]))))

        # tests whether one of the values ​​comes from the temporary positions directory above 0.9 and
        # whether the register psition directory with the same number contains the value None.
        for tpn in tpd:
            if tpd[tpn] > 0.9 and rpd["rpn_" + tpn.split("_")[-1]] == None:

                # set led color to White
                led.setColor('White')

                while True:

                    # update the convertet receiver imput into the receiver channel directory
                    tpd[tpn] = rie(int(nri.read(int(tpn.split("_")[-1]))))

                    # tests whether one of the values ​​comes from the temporary positions directory under -0.9 and
                    # whether the register psition directory with the same number contains the value None
                    if tpd[tpn] < -0.9 and rpd["rpn_" + tpn.split("_")[-1]] == None:

                        # set led color to Black
                        led.setColor('Black')

                        # set the position value in the register psition directory
                        rpd["rpn_" + tpn.split("_")[-1]] = pcn

                        # add one to psition control nummer and break the while loop
                        pcn += 1
                        break

        # tests for the value to be deleted and whether it has already been deleted
        for rpn in rpd:
            if rpd[rpn] != None and "tpn_" + rpn.split("_")[-1] in tpd:

                # deletes the previously tested value from the temporary positions directory.
                tpd.__delitem__("tpn_" + rpn.split("_")[-1])

        # the loop is interrupted when the temporary positions directory has no more value
        if tpd == dict():
            break

    # set led color to Green
    led.setColor('Green')

    # returns register psition directory
    return rpd


if __name__ == '__main__':
    print("")

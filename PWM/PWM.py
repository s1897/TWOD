from TWOD_NA2.pwm import *
from TWOD_PWM.PWM_CON import *


def pwm(engn, rcic, sp=500):
    en = PWM(engn)
    en.initialize()
    en.set_period(sp)
    en.enable()

    en.set_duty_cycle(rcic)
    return rcic

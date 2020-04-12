from TWOD_NA2.pwm import *


def pwm(engn, rcic):
    en = PWM(engn)
    en.initialize()
    en.set_period(500)
    en.enable()
    en.set_duty_cycle(rcic)
    return rcic

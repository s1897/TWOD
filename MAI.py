
# ███    ███  █████  ██
# ████  ████ ██   ██ ██
# ██ ████ ██ ███████ ██
# ██  ██  ██ ██   ██ ██
# ██      ██ ██   ██ ██

# mai = main
#
# irc = initialize receiver control
# rir = raw imput receiver
#
# rca = receiver cannal amount
# cld = construct psition directory
# ccd = construct cannal directory
#
# poa = pwm output amount
# cpd = construct pwm directory
#

# # import of RIM directories
# from RIM.RRD.cld import cld
# from RIM.RRD.ccd import ccd
#
# from RIM.irc import irc
# from RIM.rir import rir
#
# # import of PWM directory
#
# from PWM.RPD.cdd import cdd
# from PWM.RPD.cpd import cpd
#
# from PWM.ppd import ppd
# from PWM.pcd import pcd
#
#
# rca = 8
# poa = 6
#
# cld = cld(rca)
# ccd = ccd(rca)
#
# cdd = cdd(poa)
# cpd = cpd(poa)
#
#
# irc = irc(cld)
# ppd = ppd(cdd)
#
# while True:
#
#     n = rir(ccd, irc)
#     print(pcd(n, ppd, cpd))
from IMU.qar import qar
from IMU.sod import sod

sod = sod(1000)

print(sod)

while True:
    qar()

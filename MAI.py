
# ███    ███  █████  ██
# ████  ████ ██   ██ ██
# ██ ████ ██ ███████ ██
# ██  ██  ██ ██   ██ ██
# ██      ██ ██   ██ ██

# mai = main
#
# irc = initialize receiver control
# rir = raw imput receiver
# cld = construct psition directory
# ccd = construct cannal directory
# rca = receiver cannal amount
#
#

# import of required directories
from RIM.irc import irc
from RIM.rir import rir

# import of required directory
from RIM.RRD.cld import cld
from RIM.RRD.ccd import ccd
from time import sleep


rca = 8

ccd = ccd(rca)
cld = cld(rca)


cld = irc(cld)


print(cld)
sleep(5)
while True:

    ccd = rir(ccd, cld)
    print(ccd)

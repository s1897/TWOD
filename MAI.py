
# ███    ███  █████  ██
# ████  ████ ██   ██ ██
# ██ ████ ██ ███████ ██
# ██  ██  ██ ██   ██ ██
# ██      ██ ██   ██ ██

# mai = main
#
# irc = initialize receiver control
#
# rrc = register receiver channels
# rrp = register receiver psition
# rri = register reciver imput
#
# rcd = register cannal directory
# rpd = register psition directory
# rid = register imput directory
#
# rca = receiver cannal amount
#
#

# import of required directories
from RIM.irc import irc
from RIM.rir import rir

# import of required directory
from RIM.RRD.rrc import rrc
from RIM.RRD.rrp import rrp
from time import sleep


rca = 8

rcd = rrc(rca)
rpd = rrp(rca)


rpd = irc(rpd)


print(rpd)
sleep(5)
while True:

    rcd = rir(rcd, rpd)
    print(rcd)

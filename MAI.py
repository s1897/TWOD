
# ███    ███  █████  ██
# ████  ████ ██   ██ ██
# ██ ████ ██ ███████ ██
# ██  ██  ██ ██   ██ ██
# ██      ██ ██   ██ ██

# mai = main
#
# rpd = register psition directory
# rcd = register cannal directory
# rri = reads receiver input
# rrp = register receiver psition
# rrc = register receiver channels
# irc = initialisieren receiver control
# rca = receiver cannal amount
#
#

# import of required directories
from RIM.irc import irc
from RIM.rrc import rrc
from RIM.rrp import rrp
from RIM.rri import rri


rcd = rrc(rca=8)
rpd = rrp(rca=8)

rpd = (irc(rpd))

while True:

    rcd = rri(rcd, rpd)

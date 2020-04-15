
# ███    ███  █████  ██
# ████  ████ ██   ██ ██
# ██ ████ ██ ███████ ██
# ██  ██  ██ ██   ██ ██
# ██      ██ ██   ██ ██

# mai = main
#
# irc = initialisieren receiver control
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
from RIM.RRD.rri import rri


rcd = rrc(rca=8)
rpd = rrp(rca=8)
rid = rri(rca=8)

#
# rpd = (irc(rpd))

while True:

    rid = rir(rid)

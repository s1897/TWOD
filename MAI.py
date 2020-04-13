
# ███    ███  █████  ██
# ████  ████ ██   ██ ██
# ██ ████ ██ ███████ ██
# ██  ██  ██ ██   ██ ██
# ██      ██ ██   ██ ██

# mai = main
#
#
# rpd = register psition directory
# rcd = register cannal directory
#
#

# import of required directories
from RIM.rri import rri
from RIM.rrc import rrc
from RIM.rrp import rrp


rcd = rrc(rca=8)
rpd = rrp(rca=8)

rri(rcd, rpd)

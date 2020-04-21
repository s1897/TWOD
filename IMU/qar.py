
#  ██████   █████  ██████
# ██    ██ ██   ██ ██   ██
# ██    ██ ███████ ██████
# ██ ▄▄ ██ ██   ██ ██   ██
#  ██████  ██   ██ ██   ██
#     ▀▀

# qar Quaternions and Rotations
from math import asin, radians, degrees

x = 0.01
y = 0.01
z = 1000
r = 1

a = (x * x + y * y + z * z)**0.5

if not a == 0:
    x /= a
    y /= a
    z /= a

d = (x * x + y * y)**0.5

# print(x, y, z, d)

if not d == 0:
    xa = asin(x / d)
    ya = asin(y / d)
else:
    xa = radians(45)
    ya = radians(45)

if not r == 0:
    za = asin(z / r)
    da = asin(d / r)

else:
    za = radians(45)
    da = radians(45)

print(degrees(xa), degrees(ya), degrees(za), degrees(da))

# a = (x * x + y * y + z * z)**0.5
#
# print(a)

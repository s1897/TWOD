
#  ██████   █████  ██████
# ██    ██ ██   ██ ██   ██
# ██    ██ ███████ ██████
# ██ ▄▄ ██ ██   ██ ██   ██
#  ██████  ██   ██ ██   ██
#     ▀▀

# qar Quaternions and Rotations
from math import asin, radians, degrees

x = -2**0.5 / 2
y = -2**0.5 / 2
z = -1
r = 1

a = (x * x + y * y + z * z)**0.5

if not a == 0:
    x /= a
    y /= a
    z /= a

d = (x * x + y * y)**0.5

print(x, y, z, d)

if not d == 0:
    xa = asin(x / d)
    ya = asin(y / d)
else:
    xa = x
    ya = y

if not r == 0:
    za = asin(z / r)
    da = asin(d / r)

else:
    za = z
    da = d

print(degrees(xa), degrees(ya), degrees(za), degrees(da))

a = (x * x + y * y + z * z)**0.5

print(a)

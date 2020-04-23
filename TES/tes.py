# rcd = {'rcn_00': None, 'rcn_01': None, 'rcn_02': None, 'rcn_03': None, 'rcn_04': None, 'rcn_05': None, 'rcn_06': None, 'rcn_07': None}
# #
# tpd = {}
# for t in rcd:
#     tpd["tpn_" + t.split("_")[-1]] = int(t.split("_")[-1])
#
#
# tpd.__delitem__("tpn_01")
# tpd.__delitem__("tpn_02")
# tpd.__delitem__("tpn_03")
# tpd.__delitem__("tpn_04")
# tpd.__delitem__("tpn_05")
# tpd.__delitem__("tpn_06")
# tpd.__delitem__("tpn_07")
# print(tpd)
# if "tpn_00" in tpd:
#     print("l")


# while True:
#     t = []
#     for i in range(8):
#         try:
#             f = open("/sys/kernel/rcio/rcin/ch%d" % i, "r")
#             t.append(int(f.read()[:-1]))
#         except:
#             continue
#     print(t)
#
# print(open("D:/RCSQDB/myCloud/TWOD/TES/tr.txt", "r").read())
# t = {"tpn_02": None}
# for i in t:
#     print(i)

# k = list(range(5))
# t = list(range(1, 6))
#
# for g in k:
#     print(g)

# rid = {'rin_00': None, 'rin_01': 1, 'rin_02': None, 'rin_03': None, 'rin_04': None, 'rin_05': None, 'rin_06': None, 'rin_07': None}
#
# T = list(iter(rid))[0].split("_")[0]
# print(T)

# def htz(l):
#     htz = 5
#     htz += l
#
#     return htz
#
#
# print(htz(5))

# 10n*500mm / 154.508497187474
#
# f = 1
# l = 500
# la = 154.508497187474
#
# fa = (f * l) / la
#
#
# print(fa * la == f * l)

# print("Acc:" + "{:+10f}{:+10f}1".format(1.002, 2.0400395998))
# from math import asin, radians, degrees
#
# x = 1
# y = 1
# z = 0
# r = 1
#
# a = (x * x + y * y + z * z)**0.5
#
# if not a == 0:
#     x /= a
#     y /= a
#     z /= a
#
# d = (x * x + y * y)**0.5
#
# print(x, y, z, d)
#
# if not d == 0:
#     xa = asin(x / d)
#     ya = asin(y / d)
# else:
#     xa = radians(45)
#     ya = radians(45)
#
# if not r == 0:
#     za = asin(z / r)
#     da = asin(d / r)
#
# else:
#     za = radians(45)
#     da = radians(45)
#
# print((xa), (ya), (za), (da))
# 0
# # a = (x * x + y * y + z * z)**0.5
# #
# # print(a)
#
# from math import sin, acos, radians, degrees
#
#
# q = {"r": 1, "x": 0, "y": 0, "z": 0}
# qn = 0
# for i in q:
#     qn += q[i] * q[i]
# for i in q:
#     q[i] /= qn**0.5
# print(q)

t = ("1", "2", "3")
print(t[])

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

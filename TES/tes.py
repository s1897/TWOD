rcd = {'rcn_00': None, 'rcn_01': None, 'rcn_02': None, 'rcn_03': None, 'rcn_04': None, 'rcn_05': None, 'rcn_06': None, 'rcn_07': None}
#
tpd = {}
for t in rcd:
    tpd["tpn_" + t.split("_")[-1]] = int(t.split("_")[-1])


tpd.__delitem__("tpn_00")
tpd.__delitem__("tpn_01")
tpd.__delitem__("tpn_02")
tpd.__delitem__("tpn_03")
tpd.__delitem__("tpn_04")
tpd.__delitem__("tpn_05")
tpd.__delitem__("tpn_06")
tpd.__delitem__("tpn_07")
print(tpd)
if tpd == dict():
    print("lol")

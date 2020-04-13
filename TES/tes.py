rcd = {'rcn_00': None, 'rcn_01': None, 'rcn_02': None, 'rcn_03': None, 'rcn_04': None, 'rcn_05': None, 'rcn_06': None, 'rcn_07': None}
#
tpd = {}
for t in rcd:
    tpd["tpd_" + t.split("_")[-1]] = int(t.split("_")[-1])

for i in tpd:
    print(tpd[i])

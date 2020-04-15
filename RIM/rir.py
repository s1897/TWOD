
# ██████  ██ ██████
# ██   ██ ██ ██   ██
# ██████  ██ ██████
# ██   ██ ██ ██   ██
# ██   ██ ██ ██   ██

# rir = raw imput receiver
#


# import of required directories
# from RIM.rie import rie
from rie import rie


# define read receiver imput
def rir(rid):

    for rin in rid:
        rid[rin] = rie(int(open("/sys/kernel/rcio/rcin/ch{}".format(int(rin.split("_")[-1])), "r").read()[:-1]))


if __name__ == '__main__':
    rid = {'rin_00': None, 'rin_01': None, 'rin_02': None, 'rin_03': None, 'rin_04': None, 'rin_05': None, 'rin_06': None, 'rin_07': None}

    while True:
        print(rir(rid))

# while True:
#     t = []
#     for i in range(8):
#         try:
#             f = open("/sys/kernel/rcio/rcin/ch%d" % i, "r")
#             t.append(int(f.read()[:-1]))
#         except:
#             continue
#     print(t)

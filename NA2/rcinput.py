class RCInput():
    CHANNEL_COUNT = 14
    channels = []

    def __init__(self):
        for i in range(0, self.CHANNEL_COUNT):
            try:
                f = open("/sys/kernel/rcio/rcin/ch%d" % i, "r")
                self.channels.append(f)
            except:
                continue
                # print("Can't open file /sys/kernel/rcio/rcin/ch%d" % i)

    def read(self, ch):
        value = self.channels[ch].read()
        position = self.channels[ch].seek(0, 0)
        return value[:-1]


if __name__ == '__main__':
    r = RCInput()

    h = {"r_0": None, "r_1": None, "r_2": None, "r_3": None, "r_4": None, "r_5": None, "r_6": None, "r_7": None}
    p = {"p_0": 1, "p_1": 2, "p_2": 3, "p_3": 4, "p_4": 5, "p_5": 6, "p_6": 7, "p_7": 0}

    while True:

        for i in p:
            h["r_" + i.split("_")[-1]] = int(r.read(int(p[i])))

        print(h)

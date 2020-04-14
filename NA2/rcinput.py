class RCInput():
    CHANNEL_COUNT = 14
    channels = []

    def __init__(self):
        for i in range(0, self.CHANNEL_COUNT):
            try:
                # f = open("/sys/kernel/rcio/rcin/ch%d" % i, "r")
                with open("/sys/kernel/rcio/rcin/ch%d" % i) as f
                self.channels.append(f.read())
            except:
                continue
                # print("Can't open file /sys/kernel/rcio/rcin/ch%d" % i)

    def read(self, ch):
        value = self.channels[ch].read()
        position = self.channels[ch].seek(0, 0)
        return value[:-1]


from TWOD_NA2.rcinput import *
from TWOD_NA2.util import *
# from RCI_ENC import *

check_apm()

rcin = RCInput()


# def rci(rc_channl):
#     return int(rcin.read(rc_channl))

def rci(rc_channl):
    receiver_imput = int(rcin.read(rc_channl))
    Convertet_output_lowes = -1
    Convertet_output_highest = 1
    receiver_imput_lowest = 982
    receiver_imput_highest = 2006

    receiver_signal_range = receiver_imput_highest - receiver_imput_lowest

    return (((Convertet_output_highest - Convertet_output_lowes) / receiver_signal_range) * (receiver_signal_range - (receiver_imput_highest - receiver_imput))) + Convertet_output_lowes

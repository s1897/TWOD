from TWOD_RCI.RCI import rci

while True:
    receiver_imput = rci(0)
    Convertet_output_lowes = -1
    Convertet_output_highest = 1
    receiver_imput_lowest = 982
    receiver_imput_highest = 2006

    receiver_signal_range = receiver_imput_highest - receiver_imput_lowest

    return (((Convertet_output_highest - Convertet_output_lowes) / receiver_signal_range) * (receiver_signal_range - (receiver_imput_highest - receiver_imput))) + Convertet_output_lowes

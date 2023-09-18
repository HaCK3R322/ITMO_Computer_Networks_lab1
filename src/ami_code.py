import matplotlib.pyplot as plt


def ami_code(message):
    bit_width = 1  # длительность каждого бита
    time = []  # массив значений времени
    signal = []  # массив значений сигнала
    # заполнение массивов времени и сигнала

    polarity = 1

    for i, bit in enumerate(message):
        t = i * bit_width
        time.extend([t, t + bit_width / 2, t + bit_width / 2, t + bit_width])  # to draw two lines we need 4 points
        if bit == 1:
            signal.extend([polarity * 1, polarity * 1, polarity * 1, polarity * 1])
            polarity = -polarity
        else:
            signal.extend([0, 0, 0, 0])  # from 1 to 0

    # построение графика
    fig, ax = plt.subplots(figsize=(15, 2))
    ax.step(time, signal, where='post', color='r')
    ax.set_xlabel('Time')
    ax.set_ylabel('Signal')
    ax.set_ylim(-1.5, 1.5)
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels(['-1', '0', '1'])
    ax.set_xticks(range(0, 32, 1))
    ax.grid(True, axis='y')
    plt.title('AMI')
    plt.show()

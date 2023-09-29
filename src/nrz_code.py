import matplotlib.pyplot as plt


def nrz_code(message, code_name=""):
    bit_width = 1  # длительность каждого бита
    time = []  # массив значений времени
    signal = []  # массив значений сигнала
    # заполнение массивов времени и сигнала
    for i, bit in enumerate(message):
        t = i * bit_width
        time.extend([t, t + bit_width / 2, t + bit_width / 2, t + bit_width])  # to draw two lines we need 4 points
        if bit == 1:
            signal.extend([1, 1, 1, 1])
        else:
            signal.extend([0, 0, 0, 0])

    # построение графика
    fig, ax = plt.subplots(figsize=(15, 2))
    ax.step(time, signal, where='post', color='r')
    ax.set_xlabel('Time')
    ax.set_ylabel('Signal')
    ax.set_ylim(-0.5, 1.5)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['0', '1'])

    # Set the x-axis ticks and labels based on your 'message' list
    bit_indices = range(len(message))
    bit_positions = list(bit_indices)  # Keep the tick positions as they are
    ax.set_xticks(bit_positions)
    ax.set_xticklabels([''] * len(bit_positions))  # Clear the default tick labels

    # Add the 'message' labels with an offset of 0.5 from the tick positions
    for idx, bit in zip(bit_indices, message):
        ax.text(idx + 0.5, -0.7, str(bit), ha='center')

    ax.grid(True, axis='y')
    plt.title('NRZ (униполярный) ' + code_name)
    plt.show()
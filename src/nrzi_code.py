import matplotlib.pyplot as plt

def nrzi_code(message):
    bit_width = 1  # длительность каждого бита
    time = []  # массив значений времени
    signal = []  # массив значений сигнала

    current_state = 0  # Начальное состояние (0 для NRZI)

    # заполнение массивов времени и сигнала
    for i, bit in enumerate(message):
        t = i * bit_width
        time.extend([t, t + bit_width])  # for NRZI, we need two points per bit

        if bit == 1:
            current_state = 1 - current_state  # Toggle the current state for each 1 bit
        signal.extend([current_state, current_state])

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
    plt.title('NRZI (униполярный)')
    plt.show()

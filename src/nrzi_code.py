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
    ax.set_xticks(range(0, len(message) * bit_width + 1, 1))
    ax.grid(True, axis='y')
    plt.title('NRZI (униполярный)')
    plt.show()

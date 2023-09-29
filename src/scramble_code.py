def scramble(input_message):
    scrambled_message = []

    for i in range(len(input_message)):
        if i < 3:
            # If i is less than 3, we can't compute Bi-3 and Bi-5,
            # so we just XOR Ai with 0.
            scrambled_message.append(input_message[i])
        elif i < 5:
            scrambled_bit = input_message[i] ^ scrambled_message[i - 3]
            scrambled_message.append(scrambled_bit)
        else:
            # XOR Ai with Bi-3 and Bi-5
            scrambled_bit = input_message[i] ^ scrambled_message[i - 3] ^ scrambled_message[i - 5]
            scrambled_message.append(scrambled_bit)

    return scrambled_message

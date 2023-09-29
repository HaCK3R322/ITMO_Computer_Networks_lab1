def logic_code(message):
    if len(message) % 4 != 0:
        raise Exception("4B/5B Scrabling exception: сообщение должно быть кратно 4")

    _4b5b_codes_table = {
        "0000": [1, 1, 1, 1, 0],
        "0001": [0, 1, 0, 0, 1],
        "0010": [1, 0, 1, 0, 0],
        "0011": [1, 0, 1, 0, 1],
        "0100": [0, 1, 0, 1, 0],
        "0101": [0, 1, 0, 1, 1],
        "0110": [0, 1, 1, 1, 0],
        "0111": [0, 1, 1, 1, 1],
        "1000": [1, 0, 0, 1, 0],
        "1001": [1, 0, 0, 1, 1],
        "1010": [1, 0, 1, 1, 0],
        "1011": [1, 0, 1, 1, 1],
        "1100": [1, 1, 0, 1, 0],
        "1101": [1, 1, 0, 1, 1],
        "1110": [1, 1, 1, 0, 0],
        "1111": [1, 1, 1, 0, 1]
    }

    # Split the message into 4-bit chunks
    chunks = [message[i:i + 4] for i in range(0, len(message), 4)]

    encoded_message = []

    for chunk in chunks:
        # Convert the binary chunk to a string representation
        chunk_str = ''.join(map(str, chunk))

        if chunk_str in _4b5b_codes_table:
            encoded_message.extend(_4b5b_codes_table[chunk_str])
        else:
            raise Exception(f"4B/5B Scrambling exception: Invalid 4-bit chunk: {chunk_str}")

    return encoded_message

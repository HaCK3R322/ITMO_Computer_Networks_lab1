from machester_code import manchester_code
from rz_code import rz_code
from nrz_code import nrz_code
from nrzi_code import nrzi_code
from ami_code import ami_code

def main():
    ########################################
    #                ЭТАП 1                #
    ########################################
    print("========== ЭТАП 1 ==========")

    source_message = 'Андросов И.С.'
    print('Исходное сообщение: ' + source_message)

    hex_message = [0xC0, 0xED, 0xE4, 0xF0, 0xEE, 0xF1, 0xEE, 0xF2, 0x20, 0xC8, 0x2E, 0xD1, 0x2E]
    print('Шестандцатеричное представление: ', end='')
    for byte in hex_message:
        print(format(byte, '02X'), end=' ')
    print()

    print('Двоичное представление: ', end='')
    binary_message = []
    for byte in hex_message:
        binary_byte = bin(byte)[2:].zfill(8)
        binary_message.extend(int(x) for x in list(binary_byte))
    binary_message_print_count = 1
    for number in binary_message:
        print(number, end='')
        if binary_message_print_count == 8:
            print(' ', end='')
            binary_message_print_count = 1
        binary_message_print_count += 1
    print()

    ########################################
    #                ЭТАП 2                #
    ########################################
    print("\n========== ЭТАП 2 ==========")
    print("ПРОПУСКНАЯ_СПОСОБНОСТЬ = 100 Мб/с")

    binary_message_first_4_bytes = binary_message[:32]

    print("\n=== Манчестерский код: =====")
    manchester_code(binary_message_first_4_bytes)
    # Частотный спектр сигнала при манчестерском кодировании включает в себя только две частоты:
    # при скорости передачи 100 Мбит/с
    # это 100 МГц (соответствует передаваемой цепочке из одних нулей или из одних единиц)
    # и 50 МГц (соответствует последовательности из чередующихся нулей и единиц: 1010101010...
    print('Верхняя граница: 100 МГц (fв)')
    print('Нижняя граница: 50 МГц (fн)')
    print('Спектр частот: 50 МГц (S = fв-fн)')
    print('Средняя частота: ' + '82.8125 МГц')

    print("\n=== RZ код: ================")
    rz_code(binary_message_first_4_bytes)
    print('Верхняя граница: 100 МГц (fв)')
    print('Нижняя граница: 50 МГц (fн)')
    print('Спектр частот: 50 МГц (S = fв-fн)')
    print('Средняя частота: ' + '76.5625 МГц')

    print("\n=== NRZ (униполярный) код: =")
    nrz_code(binary_message_first_4_bytes)
    print('Верхняя граница: 50 МГц (fв [C/2])')
    print('Нижняя граница: 8.333 МГц (fн [C/12])')
    print('Спектр частот: 41.666 МГц (S = fв-fн)')
    print('Средняя частота: ' + '9.7656 МГц')

    print("\n=== NRZI код: =====")
    nrzi_code(binary_message_first_4_bytes)
    print('Верхняя граница: 50 МГц (fв [C/2])')
    print('Нижняя граница: 7.142 МГц (fн [C/14])')
    print('Спектр частот: 42.857 МГц (S = fв-fн)')
    print('Средняя частота: 18.764')

    print("\n=== AMI код: =====")
    ami_code(binary_message_first_4_bytes)



if __name__ == '__main__':
    main()

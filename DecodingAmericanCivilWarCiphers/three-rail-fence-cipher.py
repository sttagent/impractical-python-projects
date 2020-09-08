import math

from DecodingAmericanCivilWarCiphers.route_cipher_encoder import \
    delete_punctuation

MESSAGE = """We will run the batteries at Vicksburg the night of April 16 and
            proceed to Grand Gulf where we will reduce the forts. Be
            prepared to cross the river on April 25 or 29. Admiral Porter"""


def main():
    print("Message to encode:")
    print(MESSAGE)
    encrypted_message = encrypt_message(MESSAGE[:])
    print("\nEncrypted Message:")
    print(encrypted_message)


def encrypt_message(message):
    word_list = message.upper().split()
    delete_punctuation(word_list)
    cipher_text = "".join(word_list)
    row1, row2, row3 = split_rails(cipher_text)
    encrypted_message = encrypt(row1, row2, row3)
    return "".join(encrypted_message)


def encrypt(row1, row2, row3):
    message = []
    char_list1 = list(row1)
    char_list2 = list(row2)
    char_list3 = list(row3)
    while True:
        if char_list1:
            message.append(char_list1.pop(0))
        else:
            break
        if char_list2:
            message.append(char_list2.pop(0))
        else:
            break
        if char_list3:
            message.append(char_list3.pop(0))
        else:
            break
        if char_list2:
            message.append(char_list2.pop(0))
        else:
            break
    return message



def split_rails(cipher_text):
    cycle = 4
    num_cycles = math.floor(len(cipher_text) / cycle)
    remainder = len(cipher_text) - (cycle * num_cycles)
    if remainder == 0:
        row1_length = num_cycles
        row2_length = num_cycles * 2
    elif remainder == 1:
        row1_length = num_cycles + 1
        row2_length = num_cycles * 2
    elif remainder == 2:
        row1_length = num_cycles + 1
        row2_length = (num_cycles * 2) + 1

    row1 = cipher_text[:row1_length]
    row2 = cipher_text[row1_length:row1_length + row2_length]
    row3 = cipher_text[row1_length + row2_length:]

    return row1, row2, row3






if __name__ == '__main__':
    main()

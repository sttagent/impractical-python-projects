import sys
from collections import Counter


def main():
    file_names = ['cipher_a.txt', 'cipher_b.txt']
    for file_name in file_names:
        cipher = load_cipher_from_file(file_name)
        is_transposition_type = check_if_cipher_is_transposition_type(cipher)
        if is_transposition_type:
            print(f"Cipher in {file_name} is likely a transposition type")
        else:
            print(f"Cipher in {file_name} is likely a substitution type")


def check_if_cipher_is_transposition_type(cipher):
    cipher_length = len(cipher)
    letter_count = Counter(cipher)
    relative_frequency_of_letters = get_relative_frequency(letter_count, cipher_length)
    first_four_letters = [letter[0] for letter in relative_frequency_of_letters[:4]]
    four_most_common_letters = ['E', 'T', 'A', 'O']
    if first_four_letters == four_most_common_letters:
        cipher_is_transposition = True
    else:
        cipher_is_transposition = False
    return cipher_is_transposition


def load_cipher_from_file(file):
    try:
        with open(file) as f:
            cipher = f.read()
    except IOError as e:
        print(f"e\nCan't open the file: {file}. Terminating program.", file=sys.stderr)
        sys.exit(1)

    return cipher


def get_relative_frequency(letter_counter, cipher_length):
    letter_frequency = {}
    for letter, number in letter_counter.items():
        # the percent of how many times a letter appears compared to total
        # number of letters
        letter_frequency[letter] = (number / cipher_length) * 100

    # Sort dict by value. Result is list of tuples
    letter_frequency_sorted = sorted(
        letter_frequency.items(),
        key=lambda item: item[1],
        reverse=True)

    return letter_frequency_sorted



if __name__ == '__main__':
    main()
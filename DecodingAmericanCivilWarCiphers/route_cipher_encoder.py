import random
import math

from HelperModules.load_dictionary import load

MESSAGE = """We will run the batteries at Vicksburg the night of April 16 and
            proceed to Grand Gulf where we will reduce the forts. Be
            prepared to cross the river on April 25 or 29. Admiral Porter"""

CODE_WORDS = {
    'BATTERIES': 'HOUNDS',
    'VICKSBURG': 'ODOR',
    'APRIL': 'CLAYTON',
    '16': 'SWEET',
    'GRAND': 'TREE',
    'GULF': 'OWL',
    'FORTS': 'BAILEY',
    'RIVER': 'HICKORY',
    '25': 'MULTIPLY',
    '29': 'ADD',
    'ADMIRAL': 'HERMES',
    'PORTER': 'LANGFORD',
}

KEY = [-1, 3, -2, 6, 5, -4]


def main():
    print("The massage is:")
    print(f"\n{MESSAGE}\n")
    print("Encoding the message...")
    encoded_message = encode_message()
    print("Encoded message:")
    print(encoded_message)


def encode_message():
    word_list = MESSAGE.upper().split()
    delete_punctuation(word_list)
    substitute_code_words(word_list)
    columns, rows = calculate_columns_and_rows(word_list)
    word_matrix = [[None] * columns for i in range(1, rows + 1)]
    fill_in_word_matrix(word_matrix, word_list, columns, rows)
    fill_in_filler_words(word_matrix)
    encoded_message = convert_to_string(word_matrix)
    return encoded_message


def convert_to_string(word_matrix):
    message = ""
    for row in word_matrix:
        for column in row:
            message += " " + column
        message += '\n'
    return message


def fill_in_filler_words(word_matrix):
    dictionary = load('../Files/2of4brif.txt')
    for row in range(len(word_matrix)):
        for column in range(row):
            if not word_matrix[row][column]:
                word_matrix[row][column] = random.choice(dictionary).upper()


def fill_in_word_matrix(word_matrix, word_list, columns, rows):
    word_list_copy = word_list[:]
    for column in KEY:
        if column < 0:
            for row in range(rows-1, 0, -1):
                if word_list_copy:
                    word_matrix[row - 1][abs(column) - 1] = word_list_copy.pop(0)
                else:
                    break
        elif column > 0:
            for row in range(rows - 1):
                if word_list_copy:
                    word_matrix[row][column - 1] = word_list_copy.pop(0)
                else:
                    break

def substitute_code_words(word_list):
    for i in range(len(word_list)):
        if word_list[i] in CODE_WORDS:
            word_list[i] = CODE_WORDS[word_list[i]]


def calculate_columns_and_rows(word_list):
    columns = len(KEY)
    rows = len(word_list) / columns
    rows = math.ceil(rows) + 1
    return columns, rows


def delete_punctuation(word_list):
    punctuation = ',.!?:;'
    for i in range(len(word_list)):
        word_list[i] = word_list[i].rstrip(punctuation)



if __name__ == '__main__':
    main()

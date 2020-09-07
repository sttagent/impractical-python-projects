import sys
from DecodingAmericanCivilWarCiphers.automating_possible_keys import generate_possible_keys

ciphertext = """THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY
 AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP
"""

COLS = 4
ROWS = 6


def main():
    """Run program and print decrypted plaintext."""
    print("\nCiphertext = {}".format(ciphertext))
    print("Trying {} columns".format(COLS))
    print("Trying {} rows".format(ROWS))

    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    keys = generate_possible_keys(COLS)
    for key in keys:
        print(f"Trying key = {key}")
        translation_matrix = build_matrix(key, cipherlist)
        plaintext = decrypt(translation_matrix)
        print("Plaintext = {}".format(plaintext))
        print()


def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs. message length."""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):  # range excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    print("\nLength of cipher = {}".format(len_cipher))
    print("Acceptable column/row values include: {}".format(factors))
    print()
    if ROWS * COLS != len_cipher:
        print("\nError - Input columns & rows not factors of length "
              "of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)    


def build_matrix(key_int, cipherlist):
    """Turn every n-items in a list into a new item in a list of lists."""
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0:  # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0:  # read top-to-bottom of columnn
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix


def decrypt(translation_matrix):   
    """Loop through nested lists popping off last item to a string."""
    plaintext = ''
    for i in range(ROWS): 
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext


if __name__ == '__main__':
    main()

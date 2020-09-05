import sys


def load(file):
    loaded_text = []
    words = []
    try:
        with open(file) as f:
            loaded_text = f.read().strip().split('\n')
    except IOError as e:
        print(f"{e}\nError opening {file}. Terminating program.", file=sys.stderr)
        sys.exit(1)
    else:
        words = [word.lower() for word in loaded_text]

    return words


def remove_single_letter_words(word_list):
    filtered_list = []
    for word in word_list:
        if len(word_list) > 1:
            filtered_list.append(word)

    return filtered_list
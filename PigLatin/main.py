from pig_latin import convert_to_pig_latin


def main():
    words = ["sit", "word", "ask", "complicated"]
    for word in words:
        converted_vord = convert_to_pig_latin(word)
        print(converted_vord)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def chart_letters(sentence):
    chart = {}

    same_letter = sentence[0]
    for letter in sentence:
        if not letter.isalpha():
            continue
        if letter in chart:
            chart[letter].append(letter)
        else:
            chart[letter] = [letter]

    return chart


def display_chart(chart):
    print("{")
    for key in sorted(chart):
        print(f"'{key}': {chart[key]},")
    print("}")


def main():
    sentence = "test sentence"
    result = chart_letters(sentence)
    display_chart(result)


if __name__ == "__main__":
    main()

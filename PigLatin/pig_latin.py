def convert_to_pig_latin(word):
    is_vowel = test_if_vowel(word[0])
    if is_vowel:
        converted_word = word + 'way'

    else:
        partitioned_word = word.partition(word[0])
        converted_word = partitioned_word[2] + partitioned_word[1] + 'ay'
    return converted_word


def test_if_vowel(letter):
    vowels = ('a', 'e', 'i', 'u', 'o')
    if letter in vowels:
        is_vowel = True
    else:
        is_vowel = False

    return is_vowel

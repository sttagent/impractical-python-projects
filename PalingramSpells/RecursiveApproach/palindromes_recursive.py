import HelperModules.load_dictionary as load_dictionary

words_list = load_dictionary.load('../Files/2of4brif.txt')
palindrome_list = []

def check_if_word_is_palindrome(word):
    if len(word) < 2:
        return True
    elif word[0] == word[-1]:
        return check_if_word_is_palindrome(word[1:-1])
    else:
        return False


for word in words_list:
    is_word_palindrome = check_if_word_is_palindrome(word)
    if is_word_palindrome:
        palindrome_list.append(word)

print(f"Number of palindromes found: {len(palindrome_list)}")
print(*palindrome_list, sep='\n')

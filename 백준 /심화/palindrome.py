word = input()
def isPalindrome(word):
    list_word = list(word)

    reversed_list = list_word[::-1]

    if list_word == reversed_list :
        return "1"
    else :
        return "0"

print(isPalindrome(word))
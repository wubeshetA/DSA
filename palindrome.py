def isPalindrome(string):
    return string == string[::-1]

if __name__ == '__main__':
    print(isPalindrome("hello"))
    print(isPalindrome("madam"))  
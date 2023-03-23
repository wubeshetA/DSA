def palindrome(string):
    return string == string[::-1]

if __name__ == '__main__':
    print(palindrome("hello"))
    print(palindrome("madam"))  
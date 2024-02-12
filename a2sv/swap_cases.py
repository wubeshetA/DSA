def swap_case(s):
    a = ""
    for c in s:
        if c.isupper():
            a += c.lower()
        else:
            a += c.upper()
    return a
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
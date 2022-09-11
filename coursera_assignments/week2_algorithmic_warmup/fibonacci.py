def fibonacci_naive(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_number(n):
    if n <= 1:
        return 1

    fib = [1, 1]
    for _ in range(n-1):
            res = fib[0] + fib[1]
            fib[0] = fib[1]
            fib[1] = res
    return fib[1]



if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

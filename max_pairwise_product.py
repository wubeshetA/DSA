#!/usr/bin/python3
"""
This script demonstrates max_pairwise_product with slow and fast algorithm and
It also shows stress testing
"""
from random import randint


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):

    n = len(numbers)
    index1 = 0
    for i in range(n):
        if numbers[i] >= numbers[index1]:
            index1 = i

    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for j in range(n):
        if (j != index1) and (numbers[j] >= numbers[index2]):
            index2 = j

    return numbers[index1] * numbers[index2]


if __name__ == '__main__':
    # int(input())
    # input_numbers = list(map(int, input().split()))
    # print(max_pairwise_product(input_numbers))

    # stress testing
    while True:
        numbers = [randint(1_000_000_000, 999_999_999_999) for _ in range(5)]
        print(numbers)
        print(max_pairwise_product_fast(numbers))
        if max_pairwise_product(numbers) != max_pairwise_product_fast(numbers):
            print("failed")
            break
        else:
            print("OK")

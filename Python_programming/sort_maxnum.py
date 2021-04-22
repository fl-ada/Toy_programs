# get maximum possible number by listing integers in array 'numbers'
# 1 <= len(numbers) <= 100,000
# 1 <= elements in numbers <= 1,000

import numpy as np

def fill_digits(numbers):
    # make all elements into 3 digit numbers
    new_numbers = []
    for i in range(len(numbers)):
        if numbers[i] < 10:
            # 1-digit num
            new_numbers.append(numbers[i] * 1111)
        elif numbers[i] < 100:
            # 2-digit num
            new_numbers.append(numbers[i] * 100 + numbers[i])
        elif numbers[i] < 1000:
            # 3-digit num
            new_numbers.append(numbers[i] * 10 + int(numbers[i] / 100))
        else:
            # 1000
            new_numbers.append(numbers[i])
    return new_numbers

def get_index(new_numbers):
    return np.argsort(new_numbers)[::-1]

def sort_by_index(numbers, index):
    return [numbers[i] for i in index]

def solution(numbers):
    answer = ''
    numbers = sort_by_index(numbers, get_index(fill_digits(numbers)))
    answer = "".join([str(int) for int in numbers])
    return str(int(answer))
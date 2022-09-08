def power_numbers(*numbers, power=2):
    results = []
    for num in numbers:
        results.append(num ** power)
    return results


#print(power_numbers(1, 2, 5, 7))

# задание 2
"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    result_list = []
    for arg in num:
        flag = False
        if arg > 1:
            for i in range(2, arg):
                if (arg % i) == 0:
                    flag = True
                    break
            if not flag:
                result_list.append(arg)
    return result_list


def filter_numbers(num, filter_s):
    result_list = []
    if filter_s == EVEN:
        for arg in num:
            if (arg % 2) == 0:
                result_list.append(arg)
        return result_list
    elif filter_s == ODD:
        for arg in num:
            if (arg % 2) != 0:
                result_list.append(arg)
        return result_list
    elif filter_s == PRIME:
        return is_prime(num)
    else:
        return None


#print(filter_numbers([1, 2, 3], ODD))
#print(filter_numbers([2, 3, 4, 5], EVEN))
print(filter_numbers([0, 1, 2, 4, 5, 7, 11], PRIME))

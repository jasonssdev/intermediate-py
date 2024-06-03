# Higher Order Functions #

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(1,2,sum_five))
print(sum_two_values_and_add_value(1,2,sum_one))


# Closures

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))

print(sum_ten(1)(5))

# build a higher order function

numbers = [1, 2, 3, 4, 5]

# Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter

#case without filter
def filter_even(list:list):
    my_list = []
    for i in list:
        if i % 2 == 0:
            my_list.append(i)
    return my_list

print(filter_even(numbers))

#case with filter function (easier)
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        False

print(list(filter(is_even, numbers)))

#now with filter and lambda (shortest)
print(list(filter(lambda number: number % 2 == 0, numbers)))

# Reduce
from functools import reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))

# now with lambda
print(reduce(lambda x, y: x + y, numbers))
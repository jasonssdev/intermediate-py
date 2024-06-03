# Lambdas #
# lambdas are anonymous functions
# lambdas function cannot be typed (int, float, str, etc)

sum_two_value = lambda first_value, second_value: first_value + second_value

print(sum_two_value(7, 2))

#To type a function then regular function should be used or use Callable

from typing import Callable

sum_type = Callable[[float, float, float], float]

sum_three_value = sum_type = lambda value_one, value_two, value_three: value_one + value_two + value_three

print(sum_three_value(3, 5.3, 6.2))

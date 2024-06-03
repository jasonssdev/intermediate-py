## List Comprehension ##

#orinal list
my_first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f" This is my original list {my_first_list}")

my_range = range(10)

my_list = [i + 1 for i in my_range]
print(f" This is my original list + 1 = {my_list}")

my_list = [i * 2 for i in my_range]
print(f" This is my original list * 2 = {my_list}")

my_list = [i * i for i in my_range]
print(f" This is my original list * i = {my_list}")

def even_list(num):
    num = 2*num
    return num

def odd_list(num):
    num = 2 * num + 1
    return num

my_list = [even_list(i) for i in my_range]
print(my_list)

my_list = [odd_list(i) for i in my_range]
print(my_list)

#Fibonacci List

def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
    return a

my_list = [fibonacci(i) for i in my_range]
print(my_list)
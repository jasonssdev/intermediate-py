# file handling
import os

file_txt = open("./file.txt", "w+") # read and write

file_txt.write("Hi, my name is Jason \nmy favorite programming language is Python\nalso like JS")

# print(file_txt.read())
# print(file_txt.read(10))
# print(file_txt.readline())
# print(file_txt.readlines())

print(file_txt.readlines())

file_txt.close()

# os.remove("./file.txt")

# JSON file

import json

json_file = open("./my_file.json", "w+")

json_test = {
    "name":"Jason",
    "age":34,
    "Language":["Python", "JS", "Ruby"],
    "area":"data science"}

json.dump(json_test, json_file, indent=4)

json_file.close()

json_dict = json.load(open("./my_file.json"))
print(type(json_dict))
print(json_dict)
print(json_dict["name"])
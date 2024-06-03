# regular expression

import re

my_string_one = "This is the lesson of Regular Expression"
my_string_two = "This is not the lesson of file handling"

print(re.match("This is the lesson", my_string_one))
print(re.match("This is the lesson", my_string_two))
print(re.match("Regular Expression", my_string_one))


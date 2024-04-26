import re
# Write your code here
def twice_repeated(string):
    return re.fullmatch(r"(.+)\1",string)
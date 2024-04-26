import re
# Write your code here
def thrice_repeated(string):
    return re.fullmatch(r'(.+)\1\1', string)
# Write your code here
import re

def equals_abc(string):
    pattern = r'^abc$'
    return re.match(pattern, string)
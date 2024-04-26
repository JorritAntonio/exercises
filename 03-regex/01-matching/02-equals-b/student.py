# Write your code here
import re

def equals_b(string):
    pattern = r'^b$'
    return re.match(pattern, string)
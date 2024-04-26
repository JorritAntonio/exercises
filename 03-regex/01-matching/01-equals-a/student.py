
import re

def equals_a(string):
    pattern = r'^a$'
    return re.match(pattern, string)

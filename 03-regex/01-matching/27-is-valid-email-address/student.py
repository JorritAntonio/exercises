import re

def is_valid_email_address(string):
    return re.fullmatch(r'([a-z]*[1-9]*.*)(@)(.*uccl.be)?(.*(student.uccl.be))?')
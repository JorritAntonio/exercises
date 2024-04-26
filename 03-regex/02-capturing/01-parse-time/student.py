import re


def parse_time(string):
    pattern = re.fullmatch (r'(\d{2}:\d{2}:\d{2})(\:|\.)?(\d{3})?')
    
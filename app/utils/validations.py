import re

def only_digits(s: str) -> str:
    return re.sub(r'\D', '', s)
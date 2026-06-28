# Author @xchgll
import string

"""
Generate Pattern
"""
def pattern_gen(length):
    pattern = ""
    for u in string.ascii_uppercase:
        for l in string.ascii_lowercase:
            for d in string.digits:
                full = u+l+d
                pattern += full
                if len(pattern) >= length:
                    return pattern[:length]

"""
Calculate Offset
match: expected little endian
"""
def pattern_find(length, match, x64=False):
    bytes_match = b""

    if isinstance(match, str):
        bytes_match = bytes.fromhex(match.replace("0x","").replace("0X",""))

    elif isinstance(match, int):
        size = 8 if x64 else 4
        bytes_match = match.to_bytes(size, 'big')

    elif isinstance(match, bytes):
        bytes_match = match

    else:
        print("[Error]: Unknown type:", type(match))
        return -1

    pattern = pattern_gen(length)
    sub = bytes_match[::-1].decode()

    return pattern.find(sub)

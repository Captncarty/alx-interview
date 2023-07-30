#!/usr/bin/python3

def validUTF8(data):
    """Helper function to check if the given number is a valid continuation byte."""
    def is_continuation(byte):
        return byte >> 6 == 2

    """Iterate through each byte in the data set."""
    i = 0
    while i < len(data):
        byte = data[i]

        """Check for 1-byte character (ASCII character, i.e., 0xxxxxxx)."""
        if byte >> 7 == 0:
            i += 1
            """Check for 2-byte character (110xxxxx 10xxxxxx)."""
        elif byte >> 5 == 6 and i + 1 < len(data) and is_continuation(data[i + 1]):
            i += 2
            """Check for 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)."""
        elif byte >> 4 == 14 and i + 2 < len(data) and is_continuation(data[i + 1]) and is_continuation(data[i + 2]):
            i += 3
            """Check for 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)."""
        elif byte >> 3 == 30 and i + 3 < len(data) and is_continuation(data[i + 1]) and is_continuation(data[i + 2]) and is_continuation(data[i + 3]):
            i += 4
        else:
            """If the byte does not match any of the UTF-8 encoding patterns, return False."""
            return False

    """If all bytes are successfully validated, return True."""
    return True
# You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

# This is a simplified version of the Between Markers mission.

# The initial and final markers are always different.
# The initial and final markers are always 1 char size.
# The initial and final markers always exist in a string and go one after another.





def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.find(begin)+1:text.find(end)]
    


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')

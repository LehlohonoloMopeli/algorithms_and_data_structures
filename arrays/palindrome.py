def palindrome(word) -> bool:
    """
    Returns True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]


if __name__ == "__main__":
    print(palindrome("racecar"))
    print(palindrome("hello"))

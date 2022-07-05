def integer_reversion(number):
    """
    Reverses an integer.
    """
    
    reversed = 0
    remainder = 0

    while number > 0:
        remainder = number % 10
        reversed = reversed * 10 + remainder
        number //= 10

    return reversed


if __name__ == "__main__":
    print(integer_reversion(12345))

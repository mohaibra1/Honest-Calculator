def calculate(num_one, num_two):
    """Return the division result for two numbers.

    The second number should be greater than or equal to the first one.

    Arguments:
    num_one -- an integer by which we divide.
    num_two -- an integer to be divided by 'num_one'.
    Return values:
    If the second number is smaller, return the corresponding message.
    Otherwise, return the division result as int.
    """
    if num_two < num_one:
        return 'The second number should be greater than or equal to the first one.'
    else:
        return num_two / num_one
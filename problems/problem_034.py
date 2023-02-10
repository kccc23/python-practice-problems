# Complete the count_letters_and_digits function which
# accepts a parameter s that contains a string and returns
# two values, the number of letters in the string and the
# number of digits in the string
#
# Examples:
#   * "" returns 0, 0
#   * "a" returns 1, 0
#   * "1" returns 0, 1
#   * "1a" returns 1, 1
#
# To test if a character c is a digit, you can use the
# c.isdigit() method to return True of False
#
# To test if a character c is a letter, you can use the
# c.isalpha() method to return True of False
#
# Remember that functions can return more than one value
# in Python. You just use a comma with the return, like
# this:
#      return value1, value2


def count_letters_and_digits(s):

    count_letters = 0
    count_digits = 0

    for item in s:
        if item.isalpha():
            count_letters += 1
        elif item.isdigit():
            count_digits += 1

    # for item in s:
    #     if item in ["0","1","2","3","4","5","6","7","8","9"]:
    #         count_digits += 1
    #     elif item != "" and item != " ":
    #         count_letters += 1

    return count_letters, count_digits

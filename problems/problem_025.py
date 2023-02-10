# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):

    sum = 0

    if not values:
        return None
    else:
        for value in values:
            sum += value

        return sum


# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

import statistics

def calculate_average(values):

    if not values:
        return None
    else:
        mean_values = statistics.mean(values)
        return mean_values


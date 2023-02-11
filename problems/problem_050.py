# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

import math

def halve_the_list(full_list):

    first_list = full_list[: (math.ceil(len(full_list)/2))]

    second_list = full_list[-(int(len(full_list)/2)):]

    return first_list, second_list

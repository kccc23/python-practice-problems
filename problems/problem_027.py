# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):

    # max = values[0]

    if not values:
        return None

    # else:
    #     values.sort()
    #     return values[-1]

    # else:
    #     for value in values:
    #         if value > max:
    #             max = value
    #     return max

    return max(values)

print(max_in_list([2,5,1]))

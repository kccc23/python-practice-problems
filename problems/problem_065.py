# Write a function that meets these requirements.
#
# Name:       biggest_gap
# Parameters: a list of numbers that has at least
#             two numbers in it
# Returns:    the largest gap between any two
#             consecutive numbers in the list
#             (this will always be a positive number)
#
# Examples:
#     * input:  [1, 3, 5, 7]
#       result: 2 because they all have the same gap
#     * input:  [1, 11, 9, 20, 0]
#       result: 20 because from 20 to 0 is the biggest gap
#     * input:  [1, 3, 100, 103, 106]
#       result: 97 because from 3 to 100 is the biggest gap
#
# You may want to look at the built-in "abs" function

def biggest_gap(values):

    value_iterate = values[0]
    largest_gap = 0

    for value in values:

        if largest_gap <= abs(value - value_iterate):
            largest_gap = abs(value - value_iterate)

        value_iterate = value

    return largest_gap

print (biggest_gap([1]))

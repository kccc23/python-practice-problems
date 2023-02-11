# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4

def sum_fraction_sequence(number):

    sum = 0
    sum_str = ''

    for num in range(1,number+1):
        sum += num/(num+1)
        sum_str += (str(num) + "/" + str(num+1) + "+")

    # return sum
    return sum_str[:-1]

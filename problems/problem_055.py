# Write a function that meets these requirements.
#
# Name:       simple_roman
# Parameters: one parameter that has a value from 1
#             to 10, inclusive
# Returns:    the Roman numeral equivalent of the
#             parameter value
#
# All examples
#     * input: 1
#       returns: "I"
#     * input: 2
#       returns: "II"
#     * input: 3
#       returns: "III"
#     * input: 4
#       returns: "IV"
#     * input: 5
#       returns: "V"
#     * input: 6
#       returns: "VI"
#     * input: 7
#       returns: "VII"
#     * input: 8
#       returns: "VIII"
#     * input: 9
#       returns: "IX"
#     * input: 10
#       returns:  "X"

def simple_roman(value):

    if value == 1:
        return "I"
    elif value == 2:
        return "II"
    elif value == 3:
        return "III"
    elif value == 4:
        return "IV"
    elif value == 5:
        return "V"
    elif value == 6:
        return "VI"
    elif value == 7:
        return "VII"
    elif value == 8:
        return "VIII"
    elif value == 9:
        return "IX"
    elif value == 10:
        return "X"


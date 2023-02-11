# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

import re

def check_password(password):

    if (    6 <= len(password) <= 12
        and re.search("[a-zA-Z]", password)
        and re.search("[0-9]", password)
        and re.search("[$!@]", password)
        ):
        print ("The password is valid.")
        return True

    else:
        print("The password is not valid.")
        return False

    # if (    6 <= len(password) <= 12
    #     and any(charactor.isupper() for charactor in password)
    #     and any(charactor.islower() for charactor in password)
    #     and any(charactor.isdigit() for charactor in password)
    #     and ("$" in password or "!" in password or "@" in password)
    #     ):
    #     print ("The password is valid.")
    #     return True

    # else:
    #     print("The password is not valid.")
    #     return False

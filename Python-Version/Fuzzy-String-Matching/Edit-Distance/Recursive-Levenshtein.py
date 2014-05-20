import sys


def recursivelevenshtein(s1, len_s1, s2, len_s2):
    """
    A function to calculate the Levenshtein Distance using recursion.

    :param s1: Parent String
    :param len_s1: Length Of s1
    :param s2: pattern String
    :param len_s2: length of s2
    :rtype : int returns the levenshtein distance
    """
    if len_s1 == 0:
        return len_s2
    if len_s2 == 0:
        return len_s1
    return min(
        recursivelevenshtein(s1, len_s1 - 1, s2, len_s2) + 1,  # Deletion
        recursivelevenshtein(s1, len_s1, s2, len_s2 - 1) + 1,  # Insertion
        recursivelevenshtein(s1, len_s1 - 1, s2, len_s2 - 1) + (s1[len_s1 - 1] != s2[len_s2 - 1])  # Substitution
    )


def user_input():
    """
    The method takes two strings from the user.
    Supports Python version <= 2.7 and >= 3.3

    :return: It returns two input strings from the user
    """
    if sys.hexversion > 0x03000000:
        return input(), input()
    else:
        return raw_input(), raw_input()


def main():
    """
    It is the main controlling block

    """
    if len(sys.argv) != 3:
        print("Enter two Strings :")
        s1, s2 = user_input()
    else:
        s1, s2 = sys.argv[1], sys.argv[2]

    print(u"The Edit Distance is : {0:s}".format(str(recursivelevenshtein(s1.lower(), len(s1), s2.lower(), len(s2)))))


if __name__ == "__main__":
    main()

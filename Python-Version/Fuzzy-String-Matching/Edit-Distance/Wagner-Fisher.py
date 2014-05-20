import sys
import string


def wagner_fisher(s1, len_s1, s2, len_s2):
    """
    A function to calculate the Levenshtein Distance using
    Wagner-Fisher Algorithm.

    :param s1: Parent String
    :param len_s1: Length Of s1
    :param s2: pattern String
    :param len_s2: length of s2
    :rtype : int returns the levenshtein distance
    """
    d = {}

    #Make to use O(min(n,m)) space
    if len_s1 > len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1
    for i in range(-1, len_s1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, len_s2 + 1):
        d[(-1, j)] = j + 1

    for i in range(len_s1):
        for j in range(len_s2):
            if s1[i] == s2[j]:
                d[i, j] = d[i - 1, j - 1]
            else:
                d[(i, j)] = min(
                    d[(i - 1, j)] + 1,  # deletion
                    d[(i, j - 1)] + 1,  # insertion
                    d[(i - 1, j - 1)] + 1,  # substitution
                )
    return d[len_s1 - 1, len_s2 - 1]


def user_input():
    """
    The method takes two strings from the user.
    Supports Python version <= 2.7 and >= 3.3.

    :return: It returns two input strings from the user.
    """
    if sys.hexversion > 0x03000000:
        return input(), input()
    else:
        return raw_input(), raw_input()


def preprocess_input(s):
    """
    Takes a input and removes the punctuation's from the string.

    :param s: the string to preprocess.
    :return: returns the processed string.
    """
    for p in string.punctuation:
        s = s.replace(p, '')

    return s.lower().strip()


def main():
    """
    It is the main controlling block

    """
    if len(sys.argv) != 3:
        print("Enter two Strings :")
        s1, s2 = user_input()
    else:
        s1, s2 = sys.argv[1], sys.argv[2]

    s1, s2 = preprocess_input(s1), preprocess_input(s2)

    print(u"The Edit Distance is : {0:s}".format(str(wagner_fisher(s1, len(s1), s2, len(s2)))))


if __name__ == "__main__":
    main()

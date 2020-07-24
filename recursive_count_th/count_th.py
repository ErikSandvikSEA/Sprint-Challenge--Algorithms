"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):

    # TBC
    # base case for if we have no option for a t and h
    if len(word) < 2:
        return 0

    # work backwards from the end of the string checking if the last letter is h and the 2nd to last is t
    if word[-2] == "t" and word[-1] == "h":
        # add 1 to the counter and recurse by slicing down two slots
        return 1 + count_th(word[:-2])

    # if the 2nd to last and last letters aren't t and h,
    # call the function again on the entire word except the last character
    else:
        return count_th(word[:-1])

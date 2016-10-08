"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    words = set(words)

    return words


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    unique_common_items = set(items1) & set(items2)

    return unique_common_items


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    pairs_list = []

    numbers = sorted(set(numbers))

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 0:
                pairs_list.append([numbers[i], numbers[j]])
        if numbers[i] == 0:
            pairs_list.append([numbers[i], numbers[i]])

    return pairs_list


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    ## initialize empty dictionary to store character counts as key:val pairs
    character_count = {}

    ## verbose first attempt at creating char_count dictionary
    # for char in phrase.replace(" ", ""):
    #     if char not in character_count:
    #         character_count[char] = 0
    #     character_count[char] += 1

    ## better way to set up the dictionary!
    for char in phrase.replace(" ", ""):
        character_count[char] = character_count.get(char, 0) + 1

    ## converts char_count dictionary into a sortable pair list
    char_and_count_pairs = character_count.items()

    ## initializes empty list for the sorted pairs
    sorted_pairs = []

    ## switches the position of key:value in each tuple in the pair list
    ## such that now the char-count is at index 0 and the list can be sorted
    ## by frequency, adds the new tuple to the new sorted_pairs list
    for item in char_and_count_pairs:
        sorted_pairs.append((item[1], item[0]))

    ## sorts the list by frequency in ascending order
    sorted_pairs.sort()

    ## takes the last 1 (or 2 if a tie) item in the sorted list, which will
    ## be the most-frequently occuring letter, and creates a top_char_list with
    ## it.
    ## as-is only handles potential two-way ties
    if sorted_pairs[-1][0] == sorted_pairs[-2][0]:
        top_char_list = [sorted_pairs[-1][1], sorted_pairs[-2][1]]
    else:
        top_char_list = [sorted_pairs[-1][1]]

    ## returns the top_char_list (1-2 characters), sorted alphabetically    
    return sorted(top_char_list)


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print

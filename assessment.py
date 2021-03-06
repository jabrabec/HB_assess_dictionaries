"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    ## initialize empty dictionary to track word counts as key:val pairs
    word_count = {}

    ## split the input phrase on spaces, iterate over the resulting list on
    ## word by word basis
    for word in phrase.split():
        ## look up the value associated with word as key in dictionary;
        ## if not there, will return 0 as default then increment by 1 for a new
        ## value of 1 for the first occurrence of word; if it is there, the
        ## value will be incremented by 1
        word_count[word] = word_count.get(word, 0) + 1

    ## return final word_count dictionary
    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    ## creates melon name:price dictionary for price lookup
    melon_dict = {"Watermelon": 2.95, "Cantaloupe": 2.50, "Musk": 3.25, "Christmas": 14.25}

    ## returns the price for a melon name, if in the dictionary, otherwise
    ## returns 'No price found' if not present. Turns melon_name input to
    ## .title() to account for different input possibilities and facilitate
    ## matching to string format of dictionary keys
    return melon_dict.get(melon_name.title(), 'No price found')


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    ## initialize empty dictionary to track word lengths as key:val pairs
    word_lengths = {}

    ## iterate over the input list on a word by word basis and then char by char
    ## within the word, creating a dictionary with word as key and its length
    ## as value
    for word in words:
        ## initialize empty counter/reset count for each word in words
        count = 0
        ## iterate over all characters being read and increment count accordingly
        for char in word:
            count += 1
        ## create new dict key with empty list if count has not yet been seen
        if count not in word_lengths:
            word_lengths[count] = []
        ## append the current word as new value to existing value list for this
        ## count key in dictionary (existing value list could be empty or could
        ## contain previously seen word(s) with the same # of characters)
        word_lengths[count].append(word)

    ## iterate over value lists for word_lengths keys and sort in place
    for counts in word_lengths:
        word_lengths[counts].sort()

    ## return word_lengths dictionary in the form of a list of tuples; sorted()
    ## ensures results are sorted by tuple value at index 0
    return sorted(word_lengths.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    ## creates source dictionary for pirate translations
    pirate_dict = {"sir": "matey", "hotel": "fleabag inn", "student": "swabbie",
                   "man": "matey", "professor": "foul blaggart",
                   "restaurant": "galley", "your": "yer", "excuse": "arr",
                   "students": "swabbies", "are": "be", "restroom": "head",
                   "my": "me", "is": "be"}

    ## initializes empty list for holding translated/untranslated words
    new_phrase = []

    ## splits phrase at whitespace, converting into a list. then iterates over
    ## the list; if source word exists as key in pirate dictionary, replaces it
    ## with the translated value, otherwise keeps original word
    for word in phrase.split():
        new_phrase.append(pirate_dict.get(word, word))

    ## returns translated list in string format, joined by spaces
    return " ".join(new_phrase)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    ## initialize empty dictionary to hold input names
    names_dict = {}

    ## fill in dictionary keys with input names
    for name in names:
        if name not in names_dict:
            names_dict[name] = []

    ## fill in dictionary values by last letter of key = first letter of value
    for key in names_dict.keys():
        for name in names:
            if key[-1] == name[0]:
                names_dict[key].append(name)

    ## initialize game_result list with the first name from input at index 0
    game_result = [names[0]]

    ## initialize first dictionary key equal to the first name from input
    key = names[0]

    ## continually perform the following steps so long as each key examined
    ## in the dictionary is not paired with an empty list
    while names_dict.get(key) != []:
        ## set next name to be added to results as the first in the value list
        ## for that key in dictionary
        next_name = names_dict[key][0]
        ## double check that this name has not already been added to the
        ## game results; if it has remove it from this key's value list and
        ## return to line 244
        if next_name in game_result:
            names_dict[key].remove(names_dict[key][0])
        ## when the name does not already exist in game results:
        else:
            ## append this next name value to the game results list,
            ## remove it from the value list of its associated key:value
            ## pair, and reset the key for the next iteration
            game_result.append(next_name)
            names_dict[key].remove(next_name)
            key = next_name

    return game_result

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

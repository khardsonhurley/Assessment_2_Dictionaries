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
    #Turns the list into a set, which removes duplicates. 
    words_set = set(words)
    words_list = list(words_set)
    return words_list


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
    #Turn both lists into sets to remove any duplicates. Then turns 
    #it back into a list in order to iterate over it. 
    items1 = set(items1)
    items2 = set(items2)

    intersection = items1 & items2
    return list(intersection)

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
    #empty dictionary to add all tuples and values to. 
    addends_sums_dict = {}
    #empty list to add all keys 
    tuple_key_list = []
    #empty list to put pairs that add to zero. 
    zero_pairs = []

    #for loop to create list of all pairs as tuples. First loop gets one
    #index then goes into the second for loop in order to pair the first 
    #index with all subsequent indices. 
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            num_pair = tuple([numbers[i],numbers[j+1]])
            tuple_key_list.append(num_pair)
    
    #This loop iterates through the list of tuples. If the tuple is not 
    #in the dictionary, it adds it to the dictionary, setting the value
    #to the sum of the elements of the tuple. 
    for t in without_duplicates(tuple_key_list): 
        if t not in addends_sums_dict.keys():
            addends_sums_dict[t] = t[0]+t[1]

    #return all the keys that have a value of zero. 
    for pair in addends_sums_dict.items(): 
        #If the value is 0, meaning the sum is 0...
        if pair[1] == 0: 
            #turns the tuple into a list and sorts it to avoid duplicates.
            pairlist = sorted(list(pair[0]))
            #if the list is not in zero_pairs, it adds it. 
            if pairlist not in zero_pairs:
                zero_pairs.append(pairlist)
    
    #Is there an easier way to do this? 
    return zero_pairs


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
    #Empty dictionary. 
    letter_counts = {}
    #take out all spaces so that they are not counted. 
    phrase_no_space = phrase.replace(" ","")
    
    #iterate over the string to count the number of times a letter occurs.
    #If letter is there, add one to the value. 
    for letter in phrase_no_space:
        letter_counts[letter.lower()] = letter_counts.get(letter.lower(),0) + 1
    
    #Find the largest value.
    largest = max(letter_counts.values())

    #Empty list to put all characters with top count in it.
    top_char = []

    #Iterates through the dictionary, if the value is the largest, the key
    #is added to the top_char list. 
    for key in letter_counts:
        if letter_counts[key] == largest:
            top_char.append(key)

    return sorted(top_char)



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

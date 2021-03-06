"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""
from random import choice

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
    #Empty list to put all words (keys) into. 
    words = []
    #Empty dictionary that will be returned later. 
    word_count = {}
    #Strip white space on the right.
    phrase.rstrip()
    #Spit all words by the space and put them in words list. 
    words = phrase.split(" ")

    #Iterate through words list and make a new key if one does not exist.
    #Each time adds one to the value, counting the number of time the word
    #appears. 
    for word in words: 
        word_count[word] = word_count.get(word, 0) + 1

    #Returns dictionary with words and their counts. 
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
    #Melon price data. 
    melon_data = {'Watermelon': 2.95,
                  'Cantaloupe': 2.50,
                  'Musk': 3.25,
                  'Christmas': 14.25}
    #If the melon is one of the keys of the dictionary, print the value. 
    if melon_name in melon_data.keys():
        print melon_data[melon_name]
    #If the melon is not of of the keys, print no price found. 
    else: 
        print "'No price found'"


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
    #Empty dictionary.
    tuples = {} 
    #iterate over the list 
    for word in words: 
        length = len(word)
        #add new length to the dictionary
        values_list = tuples.get(length,[])
        #add the new word (in list) to the old list
        values_list.append(word)
        #assign the sorted values_list to the value of the length. 
        tuples[length] = sorted(values_list)

    #return list of tuples of the pairs in the dictionary.
    return tuples.items()


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
    #make a dictionary with all pairs. 
    pirate_speak = {'sir': 'matey', 'hotel': 'fleabag inn', 
                    'student': 'swabbie', 'man': 'matey', 
                    'professor': 'foul blaggart', 'restaurant':'galley',
                    'your': 'yer', 'excuse': 'arr', 'students': 'swabbies',
                    'are':'be','restroom':'head', 'my':'me', 'is':'be'}
    #Empty list, will store new words. 
    sentence = []
    #take in string, split and make list. 
    phrase.rstrip()
    words = phrase.split(" ")
    #iterate over the list, for every word, add to new list. 
    for word in words: 
        if word in pirate_speak.keys():
            new_word = pirate_speak.get(word)
            sentence.append(new_word)
        else:
            sentence.append(word)

    #String with space so when .join(sentence), words are separated
    #by spaces. 
    text = " "
    
    #Use .join to return the string. 
    return text.join(sentence)


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

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    #Since I did not have time to do this, I decided to pseudocode my ideas.
    #I realize this is a lot like the markov chain exercise. 
    
    #start with empty list to put new sentence in. 
    sentence = []

    #chose the first word from the given list to start. Add it to the new
    #list that will be used to create the sentence. 
    first_word = names[0]
    sentence.append(first_word)
    names.remove(first_word)

    #get the last letter of the first word.
    last_letter = first_word[-1]

    #look through all of the words in names, to find one whose first letter is 
    #the same as the last letter. 

    #find the word, add it to the sentence list. 

    #grab the last letter from that word

    #iterate again to find another word that starts with that letter. 

    #add it to the sentence. Keep going until there is not a match. 

#I TRIED THIS, BUT IT DOES NOT WORK PAST THE SECOND WORD, PLEASE HELP.
    #need some sort of while loop here to keep it going, cant figure out how 
    #to get past the second word. 
    for word in names: 
        if last_letter == word[0]:
            sentence.append(word)
            names.remove(word)
            word = names[0]
            last_letter = word[-1]



    return sentence

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

from random import choice
from sys import argv

N_GRAM = 4


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path, 'r') as f:
        return f.read()


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    chains = { }
    # Split on white space to get words
    words = text_string.split()

    for i in range(len(words) - N_GRAM):
        # Create tuple to hold n words
        words_ngram = tuple(words[i : i + N_GRAM ])
        # Get the last element
        element = words[i + N_GRAM]
        # If the tuple key exists, append the element to the value list 
        if words_ngram in chains:
            chains[words_ngram].append(element)
        # The tuple key doesn't exist, so create it and add the element in the value list
        else:
            chains[words_ngram] = [element]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    text = ''

    # Get the beginning tuple
    words_ngram = choice(chains.keys())
    text = " ".join(words_ngram)
    # Tuple is a key in chains dict
    while len(text) < 55000:
        # Get a random list from the given tuple
        word_list = chains.get(words_ngram)

        # Check for an empty list
        if word_list is None:
            break

        word_n = choice(word_list)

        # Make all the things strings
        text = text + " " + word_n

        # Shift over the words to get the next key
        words_ngram = words_ngram[1:] + (word_n,)

    return text

input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)


# Produce random text
random_text = make_text(chains)

print random_text
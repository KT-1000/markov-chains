from random import choice


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
    # split on white space to get words
    words = text_string.split()

    for i in range(len(words) - 2):
        word1 = words[i]
        word2 = words[i + 1] 
        element = words[i + 2]
        # If the tuple key exists, append the element to the value list 
        if (word1, word2) in chains:
            chains[(word1, word2)].append(element)
        # The tuple key doesn't exist, so create it and add the element in the value list
        else:
            chains[(word1, word2)] = [element]
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    text = ''

    # Get the beginning pair
    word1, word2 = choice(chains.keys())
    text = word1 + " " + word2 + " "
    # tuple is a key in chains dict
    while len(text) < 55000:
        # Get a random list from the given pair
        word_list = chains.get((word1, word2))
        # Check for an empty list
        if word_list is None:
            return text

        word3 = choice(word_list)

        # # Make all the things strings
        # temp_string = str(word1) + " " + str(word2) + " " + str(word3)
        # text = text + temp_string
        text += word3 + " "
        word1 = word2
        word2 = word3

    return text

input_path = "dracula.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)


# Produce random text
random_text = make_text(chains)

print random_text
print len(random_text)

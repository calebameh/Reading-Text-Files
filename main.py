# Read text from a file, and count the occurence of words in that text


from cgitb import text
from fileinput import filename
from typing import Counter

from pyparsing import Word


def read_file_content(filename):
    # read content of a .txt file
    with open(filename) as f:
        text = f.read()
    return text


# function that counts words in a .txt file

def count_words():

    # create a list of all words in the text file
    text = read_file_content("./story.txt")
    text = text.split()

    # get dictionary of unique words as keys and number of occurence as Values
    count = {}
    for word in text:
        count[word] = text.count(word)
    return count


print(count_words())

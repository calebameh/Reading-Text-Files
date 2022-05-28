# Read text from a file, and count the occurence of words in that text


from cgitb import text
from typing import Counter

from pyparsing import Word


def read_file_content(filename):
    # read content of a .txt file
    with open ("story.txt", "r") as f:
        text = f.read().replace("\n","")
        return text 
        
   
#function that counts words in a .txt file   
def count_words():
    #create a list of all words in the text file
    master_list = []
    text = read_file_content("story.txt")
    list_of_Words = text.split(" ")
    
    #print iterate words in a list and remove empty strings and \n
    for words in list_of_Words:
        master_list.append(words.replace("\n",""))
                
    #Remove empty item in the list
    new_list = []
    for x in master_list:
        if x != '':
            new_list.append(x)

    #get dictionary of unique words as keys and number of occurence as Values
    unique_words = Counter(new_list)
    dictionary_unique_words = dict(unique_words)
    print (dictionary_unique_words)
    
print (count_words())
  
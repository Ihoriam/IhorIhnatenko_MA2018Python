"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if len(list1) == 0:
        return []
    else:
        new_list = []
        for idx in range(0, len(list1) - 1):
            if list1[idx] == list1[idx + 1]:
                continue
            new_list.append(list1[idx])
        new_list.append(list1[-1])
        return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    if (len(list1) == 0 or len(list2) == 0) is True:
        return []
    else:
        new_list = []
        idx_1 = 0
        idx_2 = 0
        while idx_1 < len(list1) and idx_2 < len(list2):
            if list1[idx_1] > list2[idx_2]:
                idx_2 += 1
            elif list1[idx_1] < list2[idx_2]:
                idx_1 += 1
            else:
                new_list.append(list1[idx_1])
                idx_1 += 1
                idx_2 += 1
        return new_list


# Functions to perform merge sort

def merge(left, right):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
                
def merge_sort(arr):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return ['']
    
    all_words = []
    for string in gen_all_strings(word[1:]):
        for idx in range(len(string) + 1):
            all_words.append(string[:idx] + word[0] + string[idx:])
    return gen_all_strings(word[1:]) + all_words
    
    

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()

    
    

'''
Given a word wand a strings, find all indices ins which are the starting locations
of anagrams of w. For example, given w is ab ands is abxaba, return [ 0, 3, 4]

An anagram is a word or phrase formed 
by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

# Brute force solution to find all indices of anagrams of w in s
# Go over each word-sized window in s and check if it is an anagram of w
# O(w x s) time complexity, where w is the length of the word and s is the length of the string
# from collections import Counter
# def is_anagram(s1, s2):
#     return Counter(s1) == Counter(s2)

# def anagram_indices(word, s):
#     result = []
#     for i in range(len(s) - len(word) + 1):
#         window= s[i:i + len(word)]
#         if is_anagram(window, word):
#             result.append(i)
#     return result

# better potential strategy : hash table
'''
Notice that at each window we are recomputing
the frequency counts of the entire window, when only a small part of it actually is
updated. If we could efficiently update these frequency counts for each substring,
our algorithm would be much quicker.
This insight leads us to the following strategy. First, we make a frequency dictionary
of both the initial window and the target word. As we move along the string, we
increment the count of each new character and decrement the count of the old. If at
any point there is no difference between the frequencies of the target word and the
current window, we add the corresponding starting index to our result. 

in short:
- if frequency is empty -> anagram found
- First check for the first window (0 to len(word))
- Check for the rest of the windows by adding the start_char and removing end_char of the window
    if frequency is empty -> anagram found

'''
from collections import defaultdict

def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]

def anagram_indices(word, s):
    result = []

    freq = defaultdict(int) # frequency dictionary for word
    for char in word:
        freq[char] += 1
    print(f"Initial frequency dictionary: {dict(freq)}")

    for char in s[:len(word)]:
        print(f"Processing character: {char}")
        freq[char] -= 1
        del_if_zero(freq, char)

    print(f"Frequency dictionary after initial window: {dict(freq)}")

    if not freq:
        result.append(0)
    
    for i in range(len(word), len(s)):
        print(f"Current index: {i}")
        start_char, end_char = s[i - len(word)], s[i]
        print(f"Start character: {start_char}, End character: {end_char}")
        freq[start_char] += 1
        del_if_zero(freq, start_char)
        print(f"Frequency dictionary after adding {start_char}: {dict(freq)}")
        freq[end_char] -= 1
        del_if_zero(freq, end_char)
        print(f"Frequency dictionary after removing {end_char}: {dict(freq)}")

        if not freq:
            begging_index = i - len(word) + 1
            result.append(begging_index)
    
    return result

def main():
    # Example input
    word = "abx"
    s = "sabxabax"
    
    # Find the indices of anagrams of word in s
    indices = anagram_indices(word, s)
    
    # Print the result
    print("Input word:", word)
    print("Input string:", s)
    print("Anagram indices:", indices)

if __name__ == "__main__":
    main()
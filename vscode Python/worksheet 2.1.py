#Question 1: 
def is_symmetrical(string):
    return string == string[::-1]
def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return is_symmetrical(string)
string = "tenet"
print("String:", string)
print("Is symmetrical:", is_symmetrical(string))
print("Is palindrome:", is_palindrome(string))

#Question 2: 
def find_uncommon_words(string1, string2):
    words1 = string1.split()
    words2 = string2.split()
    word_counts = {}
    for word in words1 + words2:
        word_counts[word] = word_counts.get(word, 0) + 1
    uncommon_words = [word for word, count in word_counts.items() if count == 1]
    return uncommon_words
string1 = "The innovation on technology"
string2 = "The innovation of technology"
print("String 1:", string1)
print("String 2:", string2)
print("Uncommon words:", find_uncommon_words(string1, string2))

#Question 3: 
def add_suffix(word):
    if len(word) < 3:
        return word
    elif word[-3:] == 'ing':
        return word + 'ly'
    else:
        return word + 'ing'

word1 = 'abc'
word2 = 'string'
print(add_suffix(word1))
print(add_suffix(word2))

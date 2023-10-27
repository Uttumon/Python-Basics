string = input("Enter a string: ")

# demonstrate string in reverse
print("Original string:", string)
print("Reverse of the string is:", string[::-1])

# demonstrate string concatenation
string2 = input("Enter another string to concatenate: ")
print("Concatenated string is:", string + string2)

# demonstrate replication operator
n = int(input("Enter a number to replicate the string: "))
print("Replicated string is:", string * n)

# demonstrate relational operators
length = len(string)
print("Length of the string is:", length)
print("Length of the string is greater than 5:", length > 5)

# demonstrate membership operator
char = input("Enter a character to check its membership in the string: ")
print(char, "is present in the string:", char in string)

# demonstrate slice notation
start = int(input("Enter the start index for slicing: "))
end = int(input("Enter the end index for slicing: "))
print("Sliced string is:", string[start:end])

# demonstrate various string functions
print("Capitalized string is:", string.capitalize())
print("Count of 'A' in the string is:", string.count('A'))
print("Endswith string is:", string.endswith('e'))
print("Find in the string:", string.find('A'))
print("Index of first 'A' in the string is:", string.index('A'))
print("isalnum string is:", string.isalnum())
print("isalpha string is:", string.isalpha())
print("isdigit string is:", string.isdigit())
print("islower string is:", string.islower())
print("isupper string is:", string.isupper())
print("isspace string is:", string.isspace())
print("Length of string is:", len(string))
print("lowercase string is:", string.lower())
print("uppercase string is:", string.upper())
print("startwith string is:", string.startswith('Armature'))
print("swapcase of string is:", string.swapcase())
print("lstrip of string is:", string.lstrip())
print("rstrip of string is:", string.rstrip())


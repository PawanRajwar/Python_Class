# Use atleast two string methods and explain their purpose in the comments.


# Prompting the user to enter a sentence
# .strip() removes any leading and trailing whitespace from the input
sentence = input("Enter a sentence: ").strip()

# .lower() converts the entire string to lowercase
# This ensures that the comparison is case-insensitive
sentence_lower = sentence.lower()

# .replace() is used to replace occurrences of a specified substring with another substring
# In this case, we are replacing every occurrence of 'a' with '@'
modified_sentence = sentence_lower.replace('a', '@')

# Printing the modified sentence
print("Modified sentence:", modified_sentence)

# Explanation of the string methods used:

"""

1. .strip(): This method is used to remove any leading and trailing whitespace from the user's input. It ensures that the input is clean and doesn't include unintended spaces at the beginning or end.

2. .lower(): This method converts all characters in the string to lowercase. It's useful for normalizing the string, especially when you want to perform case-insensitive operations or comparisons.

3. .replace(): This method replaces occurrences of a specified substring with another substring. In this example, its used to replace all occurrences of the letter 'a' with '@', demonstrating how to modify specific characters or substrings within the text.

"""
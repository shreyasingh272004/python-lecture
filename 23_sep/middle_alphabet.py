#print the middle alphabet of the word
def print_middle_character(word):
    length = len(word)
    middle_index = length // 2
    if length % 2 == 0:
        # If the length is even, print the two middle characters
        print(word[middle_index - 1:middle_index + 1])
    else:
        # If the length is odd, print the middle character
        print(word[middle_index])

# Example usage
word = "Python"
print_middle_character(word)  # Output: th

word = "Programming"
print_middle_character(word)  # Output: g

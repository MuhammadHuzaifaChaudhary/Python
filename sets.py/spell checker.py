# Dictionary of correct words
dictionary = {"apple", "banana", "cherry", "date", "elderberry"}

# User input
user_words = ["apple", "bananna", "cherry", "d8te", "grape"]

# Find misspelled words
misspelled = set(user_words) - dictionary
print(f"Misspelled words: {misspelled}")  # {'bananna', 'd8te', 'grape'}

# Suggest corrections (find words with similar first letters)
for word in misspelled:
    suggestions = {w for w in dictionary if w[0] == word[0]}
    print(f"'{word}' suggestions: {suggestions}")
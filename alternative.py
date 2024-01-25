# Define a function that takes a string as input and returns a modified string

# Ask for a string from the user
user_input = input("Please enter a string: ")

# Split the string into a list of words
words = user_input.split()

# Create an empty list to store the modified words
new_words = []

# Loop through the words and change their case alternatively
for i, word in enumerate(words):
  # If the index is even, make the word lower case
  if i % 2 == 0:
    new_word = word.lower()
  # If the index is odd, make the word upper case
  else:
    new_word = word.upper()
  # Append the new word to the list
  new_words.append(new_word)

# Join the list of words into a new string
new_string = " ".join(new_words)

# Use a while loop to handle empty string exception
while True:
  try:
# Check the length of the user input
    if len(user_input) == 0:
# Raise an exception if the user input is empty
      raise Exception("Sorry, you must enter a non-empty string")
# Break the loop if the user input is valid
    break
  except Exception as e:
# Print the error message
    print(e)
# Ask the user to enter a valid string
    user_input = input('Please enter a valid String: ')
    # Print the new string
print(new_string)
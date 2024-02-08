def count_numbers(text):
  # Initialize a new dictionary.
  dictionary = {}
  # Complete the for loop to iterate through each "text" character.
  text = text.replace(' ', '')
  for element in text: # 1
    # Complete the if-statement using a string method to check if the
    # character is a number.
    if not element.isalpha() and element.isalnum(): # True
      # Complete the if-statement using a logical operator to check if
      # the number is not already in the dictionary.
      if element not in dictionary.keys():
           # Use a dictionary operation to add the number as a key
           # and set the initial count value to zero.
           dictionary[str(element)] = 0
      # Use a dictionary operation to increment the number count value
      # for the existing key.
      dictionary[str(element)] = dictionary[str(element)] + 1
  return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}
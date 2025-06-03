def get_number_of_words(text):
  number_of_words = len(text.split())
  return number_of_words

def character_counter(text):
  text = text.lower()
  char_counter = 0
  char_dict = {}

  for character in text:
    if character in char_dict:
      char_dict[character] += 1
    else:
      char_dict[character] = 1

  return char_dict

def sort_on(dictionary):
  return dictionary["num"]
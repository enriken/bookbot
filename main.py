import sys
from stats import *

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  return file_contents

def main():

  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  path_to_book = sys.argv[1]
  text = get_book_text(path_to_book)
  num_words = get_number_of_words(text)
  character_dict = character_counter(text)
  
  dict_list = []
  for key in character_dict:
    dict_list.append({"char": key, "num": character_dict[key]})

  dict_list.sort(reverse=True, key=sort_on)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")

  for item in dict_list:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["num"]}")

  print("============= END ===============")

main()

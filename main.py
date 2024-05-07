def main():
  frankenstein_book_path = "books/frankenstein.txt"
  print_report(frankenstein_book_path)

def print_report(path):
  text = get_book_text(path)
  chars_dict = get_chars_dict(text)
  chars_list = get_chars_list_from_dict(chars_dict)
  chars_sorted_list = sorted(chars_list,key=sort_on, reverse=True)

  print(f"--- Begin report of {path} ---")
  print(f"{get_num_words(text)} words found in the document")
  print("\n")

  for char_dict in chars_sorted_list:
    print(f"The '{char_dict["char"]}' character was found {char_dict["num"]} times")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_chars_dict(text):
  lowercase_text = text.lower()
  chars_dict = {}

  for char in lowercase_text:
    if not char.isalpha():
      continue

    if char not in chars_dict:
      chars_dict[char] = 1
    else:
      chars_dict[char] += 1
  
  return chars_dict

def get_chars_list_from_dict(dict):
  list = []
  for char in dict:
    list.append({ "char": char, "num": dict[char] })
  
  return list

def sort_on(dict):
  return dict["num"]

def get_num_words(text):
  words = text.split()
  return len(words)

main()

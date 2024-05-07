def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(text):
  words = text.split()
  return len(words)

def get_chars_dict(text):
  lowercase_text = text.lower()
  letter_count = {}

  for char in lowercase_text:
    if char not in letter_count:
      letter_count[char] = 1
    else:
      letter_count[char] += 1
  
  return letter_count

def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  chars_dict = get_chars_dict(text)
  print(chars_dict)

main()

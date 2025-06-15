# Importing functions from stats.py
import sys
from stats import word_count
from stats import total_characters
from stats import sorted_characters

book_path = "/home/gabe/workspace/github.com/bookbot/books/frankenstein.txt"

def get_book_text(filepath): # Reading txt file and passing into string
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main(): # Function for printing text from book
	text = get_book_text(book_path)
	print(text)

text = get_book_text(book_path)
total_chars = total_characters(text)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {word_count(text)} total words")
print("--------- Character Count -------")
sorted_chars = sorted_characters(total_chars)
for char_dict in sorted_chars:
    if char_dict["char"].isalpha():
        print(f"{char_dict['char']}: {char_dict['num']}")
print("============= END ===============")

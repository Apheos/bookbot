def get_book_text(filepath): # Reading txt file and passing into string 
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main(): # Function for printing text from book
	text = get_book_text("/home/gabe/workspace/github.com/bookbot/books/frankenstein.txt")
	print(text)

# main() # Calling function to print contents of book
text = get_book_text("/home/gabe/workspace/github.com/bookbot/books/frankenstein.txt")

from stats import word_count

word_count(text)

def word_count(book_text): # To find word count of a book
	num_words = book_text.split()
	print(len(num_words),"words found in this document")
	return len(num_words)

def total_characters(book_text):
	total_chars_dict = {}
	for chars in book_text:
		chars = chars.lower() # Converting characters to lowercase
		if chars not in total_chars_dict:
			total_chars_dict[chars] = 1 # Creating dictionary key
		else: total_chars_dict[chars] += 1 # Incrementing existing keys
	return total_chars_dict

def sorted_characters(total_chars_dict):
	sorted_list = [] # Creating an empty list to then sort later
	for chars in total_chars_dict:
		count = total_chars_dict[chars]
		sorted_dict = {
			"char": chars,
			"num": count,
		}
		sorted_list.append(sorted_dict)
	sorted_list.sort(reverse=True, key=sort_on) # Sorting the list
	return sorted_list

def sort_on(item): # Defining function for sorting
	return item["num"]


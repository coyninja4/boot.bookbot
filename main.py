from stats import *

def main():
    print(f"{get_num_words("books/frankenstein.txt")} words found in the document")
    print(number_of_characters(get_book_text("books/frankenstein.txt")))



main()
from stats import *

def main():
    book = get_book_text("./books/frankenstein.txt")
    number_words = count_words(book)
    print(f"Found {number_words} total words")
    dict_characters = count_characters(book)
    print(dict_characters)


main()

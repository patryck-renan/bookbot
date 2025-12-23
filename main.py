from stats import *

def main():
    book = get_book_text("./books/frankenstein.txt")
    number_words = count_words(book)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
    dict_characters = count_characters(book)
    lista = sort_dict(dict_characters)
    for i in lista:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


main()

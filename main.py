import sys
from stats import get_book_text, count_words, count_characters, sort_dict


def main():
    # verifica se foi passado o caminho do arquivo como segundo argumento
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_book = sys.argv[1] #Variável recebe o 2º arg da linha de comando: python3 main.py <path>
    
    # variável book recebe o texto completo
    try:
        book = get_book_text(path_book)
    except FileNotFoundError:
        print(f"Error: File not Found at {path_book}")
        sys.exit(1)

    number_words = count_words(book)         
    dict_characters = count_characters(book) 
    lista = sort_dict(dict_characters)       # transforma dict em lista de dicts e ordena

    # Exibindo relatório
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_book}...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
        
    for i in lista:
        if i["char"].isalpha(): # imprime apenas se caracter do alfabeto
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()

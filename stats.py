
def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def count_words(book_content):
    words_list = book_content.split()
    return len(words_list)

def count_characters(book_content):
    dict_characters = {}
    book = book_content.lower()

    for word in book:
        if word in dict_characters:
            dict_characters[word] += 1
        else:
            dict_characters.setdefault(f"{word}",1)

    return dict_characters

def sort_dict(dict):
    lista_dicts = []
    for char, count in dict.items():
        if char not in lista_dicts:
            lista_dicts.append({"char":char, "num":count})
    def sort_list(items):
        return items["num"]
    lista_dicts.sort(reverse=True, key=sort_list)

    return lista_dicts
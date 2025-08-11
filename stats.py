def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
def get_num_words(filepath):
    with open(filepath) as f:
        contents = f.read()
        words = contents.split()
        return len(words)
def number_of_characters(contents):
    data = contents.lower()
    characters = {}
    for i in data:
        present = i in characters
        if present == True
            characters[i] = characters[i] + 1
    return characters

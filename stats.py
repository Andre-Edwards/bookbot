def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)
    characters = get_characters(text)
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_characters(text):
    character_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

main()
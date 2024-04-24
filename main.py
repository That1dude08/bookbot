def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    num_letters = number_of_letters(text)
    chars_sorted_list = letters_dict_to_sorted_list(num_letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
def sort_on(d):
    return d["num"]

def letters_dict_to_sorted_list(num_letters):
    sorted_list = []
    for ch in num_letters:
        sorted_list.append({"char": ch, "num": num_letters[ch]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

def number_of_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    return letter_count


def number_of_words(text):
    words = text.split()
    count = 0
    for i in words:
        count += 1
    return(count)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()        

main()    



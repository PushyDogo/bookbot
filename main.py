def count_words(book_text):
    words = book_text.split()
    return words

def count_letters(words_lis):
    letter_dict = {}

    for word in words_lis:
        for c in word.lower():
            if c.isalpha():
                if c in letter_dict:
                    letter_dict[c] += 1
                else:
                    letter_dict[c] = 1

    letter_dict = dict(sorted(letter_dict.items(), key=lambda x:x[1], reverse=True))
    return letter_dict


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = count_words(file_contents)
        letter_dict = count_letters(word_list)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(word_list)} words found in the document")
        print()
        for key, value in letter_dict.items():
            print(f"The '{key}' character was found {value} times")
        print("--- End report ---")

main()
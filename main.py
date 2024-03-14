def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        number_of_words = count_words(words)
        letter_count =count_letters(words)
        print_report(number_of_words, letter_count)

def count_words(words):
    number_of_words = len(words)
    return number_of_words


def count_letters(words):

    letter_count={}
    for word in words:
        lower_string = word.lower()
        letters = [*lower_string]
        for letter in letters:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter]= 1
    return letter_count

def print_report(words, letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for letter in letters:
        print(f"The \'{letter}\' was found {letters[letter]} times")
main()

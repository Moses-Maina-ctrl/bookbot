def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        number_of_words = count_words(words)
        letter_count =count_letters(words)
        sorted_letters = sort_letter(letter_count)
        print_report(number_of_words, sorted_letters)

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

# Find the key to sort the letters with
def sort_on(dict):
    return dict["number"]

# Sort the letters, first by breaking dictionary to list with individual dict
def sort_letter(letters):
    letters_to_sort=[]
    for letter in letters:
        dict={}
        dict["letter"] = letter
        dict["number"] = letters[letter]
        letters_to_sort.append(dict)
    letters_to_sort.sort(reverse=True, key=sort_on)
    return letters_to_sort


def print_report(words, letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for letter in letters:
        print(f"The \'{letter["letter"]}\' was found {letter["number"]} times")

main()

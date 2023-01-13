def main():
    word_dictionary = {
        "hi": "A common greeting",
        "eyes": "An organ for seeing",
        "earth": "A planet in space"

    }

    word = input("Enter a word: ")
    # if word == "":
    #     break
    if word in word_dictionary:
        print(word, ":", word_dictionary[word])

main()
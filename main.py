def count_words(text):
    #words = text.split()
    return text.split()

def count_characters(text):
    lowered_text = text.lower()
    characters_dict = {}
    for character in lowered_text:
        if character.isalnum() == True:
            if character in characters_dict:
                characters_dict[character] += 1
            else:
                characters_dict[character] = 1
    return characters_dict

def print_report(character_dict, word_count):
    character_list = list(character_dict.items())

    def character_sort(character_list):
        return character_list[1]

    character_list.sort(reverse=True, key=character_sort)

    print("-----Begin Report-----")
    print(f"{word_count} words found in this document\n")
    for character, count in character_list:
        print(f"the character '{character}' was found {count} times")

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        text = f.read()
    
    word_count = len(count_words(text))
    character_count = count_characters(text)

    print_report(character_count, word_count)


main()
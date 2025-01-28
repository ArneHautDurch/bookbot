def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

def count_words(file_contents):
    words = len(file_contents.split())
    return words

def count_characters(file_contents):
    count_character = {}
    lowered_string = file_contents.lower()
    for character in lowered_string:
        count_character[character] = count_character.get(character, 0) + 1
    return count_character

def print_report(count_words, count_characters):
    header = "--- Begin report of books/frankenstein.txt ---"
    words = f"{count_words} words found in the document"
    
    def sort_on(count_characters_item):
        return count_characters_item["count"]

    count_characters_sort_on = [] 
    for char, count in count_characters.items():
        if char.isalpha():
            count_characters_sort_on.append({"char": char, "count": count})
    count_characters_sort_on.sort(key=sort_on, reverse=True)

    characters = ""
    for item in count_characters_sort_on:
            characters += f"The '{item['char']}' character was found '{item['count']}' times\n"
    end = "--- End report ---"
    report = header + "\n" + words + "\n\n" + characters + end
    return report

file_content = main()
word_count = count_words(file_content)
character_count = count_characters(file_content)
print(print_report(word_count, character_count))
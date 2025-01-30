def word_count(content):
    words = content.split()
    return len(words)

def char_count(content):
    char_dict = {}
    file_contents = content.lower()
    for char in file_contents:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    char = char_count(file_contents)
    char_list = [{"char": k, "count": v} for k, v in char.items()]
    new_list = []
    for item in char_list:
        if item["char"].isalpha():
            new_list.append(item)
    new_list.sort(reverse=True ,key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"${word_count(file_contents)} words found in the document")
    print("")
    for item in new_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")

main()

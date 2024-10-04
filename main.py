
def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        print(f"Number of words: {count_words(contents)}")
        print(f"Character counts: {count_characters(contents)}")

def count_words(string: str) -> int:
    return len(string.split())

def count_characters(string: str) -> dict[str, int]:
    character_dict: dict = {}
    lowered_string = string.lower()
    for i, c in enumerate(lowered_string):
        if c in character_dict:
            character_dict[c] = character_dict[c] + 1
        else:
            character_dict[c] = 1

    return character_dict


if __name__ == "__main__":
    main()

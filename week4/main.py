import json
import difflib

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def find_definition(word, dictionary):
    word = word.lower()  # Convert to lowercase for case-insensitive matching
    if word in dictionary:
        return dictionary[word]
    else:
        # Find similar words using difflib and suggest the closest one
        closest_matches = difflib.get_close_matches(word, dictionary.keys())
        if closest_matches:
            suggestion = closest_matches[0]
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return "Word not found in the dictionary."

def main():
    file_path = "dictionary.json"  # Path to your dictionary JSON file
    dictionary = load_dictionary(file_path)

    while True:
        word = input("Enter a word to find its definition (type 'quit' to exit): ")
        if word.lower() == 'quit':
            break
        definition = find_definition(word, dictionary)
        print(definition)

if __name__ == "__main__":
    main()

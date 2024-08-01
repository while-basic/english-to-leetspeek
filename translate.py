def translate_to_leetspeak(text):
    leetspeak_dict = {
        'A': '4', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6',
        'H': '#', 'I': '1', 'J': 'J', 'K': 'K', 'L': '1', 'M': 'M', 'N': 'N',
        'O': '0', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': '$', 'T': '7', 'U': 'U',
        'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '2',
        'a': '4', 'b': '8', 'c': '(', 'd': 'D', 'e': '3', 'f': 'F', 'g': '6',
        'h': '#', 'i': '1', 'j': 'J', 'k': 'K', 'l': '1', 'm': 'M', 'n': 'N',
        'o': '0', 'p': 'P', 'q': 'Q', 'r': 'R', 's': '$', 't': '7', 'u': 'U',
        'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': '2'
    }
    return ''.join([leetspeak_dict.get(c, c) for c in text])

def main():
    print()
    print("Welcome to the Leetspeak Translator!")
    print()
    while True:
        text = input("Enter text to translate (or 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Goodbye!")
            break
        translated_text = translate_to_leetspeak(text)
        print()
        print("Leetspeak: " + translated_text)
        print()


if __name__ == "__main__":
    main()


char_to_morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

morse_to_char_dict = {v: k for k, v in char_to_morse_dict.items()}









def main():
    while True:
        print("\n--- Morse Code Converter ---")
        print("1. Text → Morse")
        print("2. Morse → Text")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            user_text = input("Enter text to convert to Morse: ")
            morse_text = ''
            for char in user_text:
                morse_text += char_to_morse_dict.get(char.upper(), '')
                morse_text += ' '  # ξεχωρίζει τα Morse symbols
            print("Morse code:", morse_text)

        elif choice == '2':
            user_morse = input("Enter Morse code to convert to text (use spaces between letters, / for space): ")
            text = ''
            for morse_char in user_morse.split(' '):
                text += morse_to_char_dict.get(morse_char, '')
            print("Text:", text)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

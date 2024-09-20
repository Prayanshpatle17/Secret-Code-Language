'''SECRET CODE LANGUAGE '''

import random
import string

# Function to generate random characters
def get_random_chars(length=3):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Encoding function
def encode(sentence):
    words = sentence.split()  # Split the sentence into words
    modified_words = []

    for word in words:
        if len(word) >= 3:  # If the word has at least 3 letters
            modified_word = word[1:] + word[0]  # Remove first letter and append it to the end
            random_prefix = get_random_chars()  # Add random characters at the start
            random_suffix = get_random_chars()  # Add random characters at the end
            modified_word = random_prefix + modified_word + random_suffix
        else:
            modified_word = word[::-1]  # Simply reverse the word if it's less than 3 letters
        modified_words.append(modified_word)

    return ' '.join(modified_words)  # Return the modified sentence

# Decoding function
def decode(sentence):
    words = sentence.split()  # Split the sentence into words
    modified_words = []

    for word in words:
        if len(word) >= 9:  # If the word was encoded (3 random chars at start and end)
            stripped_word = word[3:-3]  # Remove the 3 random characters from both ends
            modified_word = stripped_word[-1] + stripped_word[:-1]  # Move last letter to the front
        else:
            modified_word = word[::-1]  # Simply reverse the word if it's less than 3 letters
        modified_words.append(modified_word)

    return ' '.join(modified_words)  # Return the decoded sentence

# Main program
def main():
    mode = input("Do you want to encode or decode? ").strip().lower()

    if mode == "encode":
        sentence = input("Enter the sentence to encode: ")
        encoded_sentence = encode(sentence)
        print("Encoded sentence:", encoded_sentence)

    elif mode == "decode":
        sentence = input("Enter the sentence to decode: ")
        decoded_sentence = decode(sentence)
        print("Decoded sentence:", decoded_sentence)

    else:
        print("Invalid choice! Please choose 'encode' or 'decode'.")

# Run the main program
if __name__ == "__main__":
    main()


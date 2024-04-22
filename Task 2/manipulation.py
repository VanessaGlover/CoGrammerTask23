def get_user_input():
    """
    Prompt the user to enter a sentence and return it.
    """
    while True:
        user_input = input("Enter a sentence: ")
        if user_input.strip():  # Check if input is not empty after stripping whitespace
            return user_input.strip()  # Remove leading/trailing whitespace
        else:
            print("Please enter a non-empty sentence.")


def calculate_sentence_length(sentence):
    """
    Calculate and return the length of the input sentence.
    """
    return len(sentence)


def replace_last_letter_with_at(sentence):
    """
    Replace every occurrence of the last letter in the sentence with '@'
    and return the modified sentence.
    """
    last_letter = sentence[-1]
    modified_sentence = sentence.replace(last_letter, '@')
    return modified_sentence


def reverse_last_three_characters(sentence):
    """
    Return the last 3 characters of the sentence in reverse order.
    """
    return sentence[-3:][::-1]


def extract_five_letter_word(sentence):
    """
    Extract and return a five-letter word from the sentence.
    If the sentence has less than 5 characters, return None.
    """
    if len(sentence) >= 5:
        five_letter_word = sentence[:3] + sentence[-2:]
        return five_letter_word
    else:
        return None


def main():
    # Get the user input
    user_input = get_user_input()

    # Calculate and display the length of the sentence
    length_of_sentence = calculate_sentence_length(user_input)
    print(f"The length of the entered sentence is: {length_of_sentence}")

    # Replace last letter with '@' and print the modified sentence
    modified_sentence = replace_last_letter_with_at(user_input)
    print(f"Original sentence: {user_input}")
    print(f"Modified sentence: {modified_sentence}")

    # Print last 3 characters in reverse order
    last_three_characters = reverse_last_three_characters(user_input)
    print(f"Last 3 characters in reverse order: {last_three_characters}")

    # Extract and print a five-letter word if possible
    five_letter_word = extract_five_letter_word(user_input)
    if five_letter_word:
        print(f"Five-letter word: {five_letter_word}")
    else:
        print("The sentence does not have enough characters to form a five-letter word.")


if __name__ == "__main__":
    main()

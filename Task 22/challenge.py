def add_prefix_un(word):
    # Add the prefix "un" to the word
    return "un" + word

# Test the function
print(add_prefix_un("happy"))  

def make_word_groups(vocab_words):
    # Extract the prefix from the first element of the list
    prefix = vocab_words[0]
    # Apply the prefix to each word in the list and join them with "::"
    prefixed_words = [prefix + word for word in vocab_words[1:]]
    # Join the prefixed words with "::"
    return " :: ".join(prefixed_words)

# Test the function
print(make_word_groups(["en", "close", "large", "able"]))  
print(make_word_groups(["pre", "fix", "view", "dict"]))   
print(make_word_groups(["auto", "matic", "graph", "mobile"]))  
print(make_word_groups(["inter", "act", "national", "twine"]))  

def remove_suffix_ness(word):
    # Check if the word ends with "ness"
    if word.endswith("ness"):
        # Remove "ness" from the end of the word
        root_word = word[:-4]
        # Check if the root word ends with a consonant followed by 'i'
        if root_word[-1] == 'i' and root_word[-2].isalpha() and root_word[-2].lower() not in ['a', 'e', 'i', 'o', 'u']:
            # Restore 'y' to 'i'
            root_word = root_word[:-1] + 'y'
        return root_word
    else:
        return word

# Test the function
print(remove_suffix_ness("heaviness"))  # Output: happy
print(remove_suffix_ness("sadness"))   # Output: kind

def adjective_to_verb(sentence, index):
    # Split the sentence into words
    words = sentence.split()
    # Get the word at the specified index
    adjective = words[index].rstrip('.').rstrip(',')
    # Add the "en" suffix to the adjective to form a verb
    verb = adjective + "en"
    return verb

# Test the function
print(adjective_to_verb("I need to make that bright.", -1 ))  
print(adjective_to_verb("It got dark as the sun set.", 2))  




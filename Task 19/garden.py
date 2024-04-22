import spacy

# Load the English model for spaCy
nlp = spacy.load('en_core_web_sm')

# Define the list of garden path sentences
gardenpathsentences = [
    "The old man the boats.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill never here hurts.",
    "The cotton clothing is made of grows in Mississippi"
]

# Tokenize each sentence and perform named entity recognition
for sentence in gardenpathsentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    print("Tokens:")
    for token in doc:
        print(token.text, token.pos_, token.tag_, token.dep_)
    print("Named Entities:")
    for entity in doc.ents:
        print(entity.text, entity.label_, spacy.explain(entity.label_) )
    print("\n")

# 1. "GPE" (Geopolitical entity) - This entity refers to countries, cities, states.
#    Explanation: The entity "Mississippi" was tagged as GPE, indicating it's a geopolitical entity.
#    It makes sense as "Mississippi" is a state in the United States.
# 2. "PERSON" - This entity refers to people, including fictional.
#    Explanation: In the sentence "Mary gave the child a Band-Aid.", "Mary" was tagged as PERSON.
#    It makes sense as "Mary" is a person's name, indicating the giver of the Band-Aid.
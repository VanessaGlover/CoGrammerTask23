import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# The similarity between "cat" and "monkey" might be relatively low since these two words represent different animals with distinct characteristics and features. 
#  Cats and monkeys belong to different biological families, and their physical attributes, behaviors, and habitats are generally dissimilar.

# The similarity between "banana" and "monkey" could be higher compared to the similarity between "cat" and "monkey". 
# This might be due to the common association between monkeys and bananas in popular culture and media. 
# The similarity between "banana" and "cat" might be the lowest among the three pairs. "Banana" and "cat" are typically unrelated in terms of semantic meaning and usage.

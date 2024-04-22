import spacy
import pandas as pd

# Load the English model with word vectors
nlp = spacy.load('en_core_web_md')

# Defining the movie descriptions and titles
movies = {
    "Movie A": "When Hiccup discovers Toothless isn't the only Night Fury, he must seek 'The Hidden World', a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
    "Movie B": "After the death of Superman, several new people present themselves as possible successors.",
    "Movie C": "A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
    "Movie D": "A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.",
    "Movie E": "A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed."
}

def recommend_movie(description):

    doc_input = nlp(description)

    # Calculates the similarity scores between the input description and each movie description
    similarity_scores = {}
    for movie_title, movie_description in movies.items():
        doc_movie = nlp(movie_description)
        similarity_scores[movie_title] = doc_input.similarity(doc_movie)

    # Finding the title of the most similar movie
    most_similar_movie = max(similarity_scores, key=similarity_scores.get)
    return most_similar_movie

# Testing the function with the description of "Planet Hulk"
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
recommended_movie = recommend_movie(description)
print("Recommended movie:", recommended_movie)

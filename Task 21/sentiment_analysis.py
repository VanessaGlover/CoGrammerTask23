import pandas as pd
import spacy

# Load the spaCy model for natural language processing
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    # Remove punctuation and convert text to lowercase
    cleaned_text = text.lower().strip()
    cleaned_text = ''.join([char for char in cleaned_text if char.isalnum() or char.isspace()])
    return cleaned_text

def remove_stopwords(text):
    # Remove stop words
    doc = nlp(text)
    cleaned_text = ' '.join([token.text for token in doc if not token.is_stop])
    return cleaned_text

def analyse_sentiment(text):
    # Analyse the sentiment of the text
    doc = nlp(text)
    sentiment_score = 0
    num_tokens = 0

    for token in doc:
        # Check if the token is a stop word or punctuation
        if not token.is_stop and not token.is_punct:
            sentiment_score += token.sentiment
            num_tokens += 1

    # Calculate average sentiment score
    if num_tokens > 0:
        avg_sentiment_score = sentiment_score / num_tokens
        if avg_sentiment_score > 0:
            return "Positive"
        elif avg_sentiment_score < 0:
            return "Negative"
        else:
            return "Neutral"
    else:
        return "Neutral"

if __name__ == "__main__":
    # Load the dataset
    dataframe = pd.read_csv('amazon_product_reviews.csv')
    
    # Clean the data
    dataframe['cleaned_text'] = dataframe['review.text'].apply(clean_text)
    dataframe['cleaned_text'] = dataframe['cleaned_text'].apply(remove_stopwords)
    
    # Remove missing values
    clean_data = dataframe.dropna(subset=['cleaned_text'])
    
    # Test the sentiment analysis function
    sample_reviews = [
        "amazon kindle is always the best ebook, upgrade every new model",
        "Fantastic product and does exactly as described. Great gift idea!",
        "I bought my Kindle about 2 months ago and the battery is already dead and will not charge",
        "It's beyond my expectation, and it can even show music score. Not fast turning though."
    ]
    
    print("Sentiment Analysis Results:")
    for review in sample_reviews:
        sentiment = analyse_sentiment(review)
        print(f"Review: {review}")
        print(f"Sentiment: {sentiment}")
        print()

import pandas as pd
import spacy

# Load the spaCy model for natural language processing
nlp = spacy.load("en_core_web_sm")

# Loading the dataset
data = pd.read_csv('amazon_product_reviews.csv')

# Selecting two product reviews for comparison (indexing starts from 0)
review1 = data['review.text'][5]  # Select the first review
review2 = data['review.text'][12]  # Select the second review

# Processing the reviews using spaCy
doc1 = nlp(review1)
doc2 = nlp(review2)

# Calculating the similarity between the two reviews
similarity_score = doc1.similarity(doc2)

# Printing the similarity score
print(f"Similarity Score between review 1 and review 2: {similarity_score}")



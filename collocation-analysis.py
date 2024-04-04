import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def perform_collocation_analysis(file_path):
    """Perform collocation analysis on a given text file to find top bigrams, excluding those that occur only once."""
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text, remove non-alphabetic tokens, and convert to lowercase
    tokens = word_tokenize(text)
    words = [word.lower() for word in tokens if word.isalpha()]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # Initialize Bigram Finder
    bigram_measures = BigramAssocMeasures()
    bigram_finder = BigramCollocationFinder.from_words(filtered_words)

    # Apply frequency filter to exclude bigrams that occur only once
    bigram_finder.apply_freq_filter(2)

    # Find the top 10 bigrams using PMI
    top_bigrams = bigram_finder.nbest(bigram_measures.pmi, 15)

    return top_bigrams

file_path = "TextFile.txt"
top_bigrams = perform_collocation_analysis(file_path)

# Print the results to the terminal
print("Top Bigram Collocations (excluding those occurring only once):")
for bigram in top_bigrams:
    print(f"{bigram[0]} {bigram[1]}")

print("\nCollocation analysis is complete.")

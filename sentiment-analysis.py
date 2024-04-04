import nltk 
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

#Download the VADER lexicon for sentiment analysis 
nltk.download('vader_lexicon')

#Read the text from the file 
with open('BarackObama1.txt', 'r') as file:
    text = file.read()

#Tokenize the text into words 
words = nltk.word_tokenize(text)
chunk_size = 100 #Splits the words into 100 word chunks
textchunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]

#Start the SentimentIntensityAnalyzer
senti = SentimentIntensityAnalyzer()
sentiments = [] #List's the setiment scores for each chunk

#Loops through each chunk of the text
for chunk in textchunks:
    chunk_text = ' '.join(chunk)  
    sentiment_score = senti.polarity_scores(chunk_text)['compound'] #Calculates the score for each chunk
    sentiments.append(sentiment_score) #Appends the sentiment score to the list 

#Plots the sentiment score
plt.plot(sentiments, marker="o", linestyle="-", color="b")
plt.xlabel('Chunk Index')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Analysis in 100-word Chunks')
plt.grid(True)
plt.show() #Shows the plot 

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter  

#Download necassaary NLTK resources 
nltk.download('punkt')
nltk.download('stopwords')

#Read the text from the file 
with open('BarackObama1.txt', 'r') as file:
    text = file.read()  

#Tokenize the text into words 
words = word_tokenize(text.lower())

#Set of English stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.isalpha() and word not in stop_words] #Filter's out stopwrds and non-alphabetic words
word_freq = Counter(filtered_words) #Counts the word frquency of each word

total_words = len(filtered_words) #Total number of words
relative_freq = {word: freq / total_words for word, freq in word_freq.items()} #Calculated the relative frequency of each word  

top_30_words = dict(sorted(relative_freq.items(), key=lambda item: item[1], reverse=True)[:30]) #Gets the top 30 words

#Prints the top 30 words with there relative frequency 
for word, freq in top_30_words.items():
    print(f"{word}: {freq:.2%}")
# About this Repository

This repository is contains the code for Harry O'Callaghan's Final-year Project for his BA in Digital Humanities & Information Technology (CK118) at University College Cork. The project, "Macroanalysing US Presidential Speeches", uses Natural Language Proccessing to analyse selected political speeches.

# Data

The dataset used for this analysis included: 

List

These files were extracted from:
Link to dataset

# Libraries

Two libraries were used to complete this project: 

1. Natural Language Toolkit [https://www.nltk.org/](https://www.nltk.org/)
2. Stylo [https://cran.r-project.org/package=stylo](https://cran.r-project.org/package=stylo)

# Scripts

## keyword-extraction.py

Keyword extraction is a technique used in natural language processing (NLP) to automatically identify the most important words or phrases in a text. 
The Code reads a text file, then filters out common english stopwords and non-and non-alphabetic words, then calculates and prints the top 30 words based on their relative frequency in the document.

## collocation-analysis.py

Collocation analysis in natural language processing identifies pairs or groups of words that often appear together in a given text
The code analyzes text from a given text file. It indentifies and prints the top 15 signifigant word pairs(bigrams)based on their co-occurrence frequency.

## sentiment-analysis.py

Sentiment analysis is a natural language processing technique that involves analyzing and determining the sentiment or emotion expressed in a piece of text
The code performs sentiment analysis on text from "textfile.txt", dividing it into 100-word chunks, calculating sentiment scores with VADER lexicon, and plots the sentiment scores to visualize the sentiment trends throughout the text.


## Craig's Zeta analysis

I also used the R-package Stylo, see:

`Eder M, Rybicki J, Kestemont M (2016). “Stylometry with R: a package for computational text analysis.” R Journal, 8(1), 107–121. https://journal.r-project.org/archive/2016/RJ-2016-007/index.html.`

Stylo was used to complete a Craig Zeta Analysis, using the package's `oppose()` function.

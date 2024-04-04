# About this Repository

This repository is contains the code for Harry O'Callaghan's Final-year Project for his BA in Digital Humanities & Information Technology (CK118) at University College Cork. The project, "Macroanalysing US Presidential Speeches", uses Natural Language Proccessing to analyse selected political speeches.

# Data

The dataset used for this analysis included: 

Inaugural Speeches

1. Harry S. Truman - January 20, 1961: Inaugural Address 
2. John F.Kennedy - January 20, 1961: Inaugural Address
3. Ronald Reagan - January 20, 1981: First Inaugural Address
4. George W. Bush - January 20, 2001: First Inaugural Address
5. Barack Obama - January 20, 2009: Inaugural Address
6. Donald Trump - January 20, 2017: Inaugural Address

Comparision Speeches

1. Harry S. Truman - March 12, 1947: Truman Doctrine
2. George W. Bush - November 6, 2003: Remarks on Freedom in Iraq and Middle East
3. John F. Kennedy - October 22, 1962: Address on the Buildup of Arms in Cuba
4. Barack Obama - March 22, 2016: Remarks to the People of Cuba
5. Ronald Reagan - September 14, 1986: Speech to the Nation on the Campaign Against Drug Abuse
6. Donald Trump - March 19, 2018: Remarks on Combating the Opioid Crisis







































These files were extracted from:
https://www.kaggle.com/datasets/kboghe/presidentialspeeches/data?select=1presidential_speeches_with_metadata.xlsx

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

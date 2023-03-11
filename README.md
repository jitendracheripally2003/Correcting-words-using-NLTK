# Correcting Words using NLTK in python
This repository is the detailed explanation and code for spelling auto correction using NLP.

We are going to use two methods for spelling correction. Each method takes a list of misspelled words and gives the suggestion of the correct word for each incorrect word. It tries to find a word in the list of correct spellings that has the shortest distance and the same initial letter as the misspelled word. It then returns the word which matches the given criteria. The methods can be differentiated on the basis of the distance measure they use to find the closest word.  ‘words’ package from nltk is used as the dictionary of correct words.

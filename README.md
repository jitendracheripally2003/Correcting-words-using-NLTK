# Correcting Words using NLTK in python
This repository is the detailed explanation and code for spelling auto correction using NLP.
For spelling correction, we're going to employ two strategies. Each technique uses a list of misspelled words and suggests a replacement term for each mistaken word. It looks for a word with the same initial letter as the misspelled word that is closest to it in the list of accurate spellings. The word that meets the specified parameters is then returned. On the premise of the distance metric they employ to identify the closest word, the methods can be distinguished.  The dictionary of appropriate terms is provided by the `nltk` package `words`.

## Method 1: Using Jaccard distance Method
The Jaccard distance, which measures the dissimilarity between two sample groups, is the opposite of the Jaccard coefficient. By deducting the Jaccard parameter from 1, we can calculate the Jaccard distance. We can also obtain it by multiplying the union's size by the ratio of the sizes of the overlap of the two sets. Instead of using tokens, we use Q-grams, which are equal to N-grams and are referred to as characters. The following formula yields the Jaccard Distance.

**Dj(A,B) = 1 - J(A,B)  = (|AB| - |AB|)/|AB|**

### Importing and Downloading:
We import `nltk`, `jaccard_distance` and `ngrams`.
We also download the `words` resource from `nltk.downloads` and assign it to `crt_wrds`.

### Calculating:
We define a function `auto_crt()` in which we calculate the Jaccard distance of the incorrect word with each correct spelling word having the same initial letter in the form of [bigrams of characters](https://www.geeksforgeeks.org/python-bigram-formation-from-given-list/). We then sort them in ascending order so the shortest distance is on top and extract the word corresponding to it and return it.

### Executing:
We take input from you as list and run it through the words in it.
You can see the magic of n-grams here and find the correct spelling of the given incorrect word.

## Method 2: Using Edit distance Method
Edit Distance measures dissimilarity between two strings by finding the minimum number of operations needed to transform one string into the other. The transformations that can be performed are:

- Inserting a new character: 
> bat -> bats (insertion of 's')

- Deleting an existing character. 
> care -> car (deletion of 'e')

- Substituting an existing character.
> bin -> bit (substitution of n with t)

- Transposition of two existing consecutive characters. 
> sing -> sign (transposition of ng to gn)

### Importing and Downloading:
Import `nltk` and `edit_distance`.
We also download the `words` resource from `nltk.downloads` and assign it to crt_wrds.

### Calculating:
Define a function `auto_crt()` in which we calculate the Edit distance of the incorrect word with each correct spelling word having the same initial letter. We then sort them in ascending order so the shortest distance is on top and extract the word corresponding to it and retrun it.

### Executing:
We take input from you as list and run it through the words in it as same as the above method.
This method gives us the output according to the shortest distance. Therefore, it can change for the same inputs in different outputs.

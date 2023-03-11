# importing the nltk suite 
import nltk

# importing jaccard distance and ngrams from nltk.util
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams

# Downloading and importing package 'words' from nltk corpus
nltk.download('words')
from nltk.corpus import words

# Assinging to variable
crt_wrds = words.words()

# finding correct spellings based on jaccard distance and retruning the correct word
def auto_crt(wrd):
    temp = [(jaccard_distance(set(ngrams(wrd, 2)),set(ngrams(w, 2))),w) for w in crt_wrds if w[0]==wrd[0]]
    return(sorted(temp, key = lambda val:val[0])[0][1])
  
# taking input from you
in_wrds=list(input("Enter words:").split(","))

# looping the list you have given and calling the auto corrector to print
for wrd in in_wrds:
    print(auto_crt(wrd.lower()))

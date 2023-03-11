# importing the nltk suite
import nltk

# importing edit distance
from nltk.metrics.distance import edit_distance

# Downloading and importing package 'words'
nltk.download('words')
from nltk.corpus import words

# Assigning to variable
crt_wrds = words.words()

# loop for finding correct spellings based on edit distance and printing the correct words
def auto_crt(wrd):
	temp = [(edit_distance(wrd, w),w) for w in crt_wrds if w[0]==wrd[0]]
	return(sorted(temp, key = lambda val:val[0])[0][1])

# taking input from you
in_wrds=list(input("Enter words:").split(","))

# looping the list you have given and calling the auto corrector to print
for wrd in in_wrds:
    print(auto_crt(wrd.lower()))

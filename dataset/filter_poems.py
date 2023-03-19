from pathlib import Path
from langdetect import detect_langs
import pandas as pd
import string
import re


def detect_english(poem, min_prob):
    # creates a list of language probabilties
    lang_probabilities = detect_langs(poem)

    is_english = False

    for probability in lang_probabilities:
        # if probability of english > 97% then it should be english
        if probability.lang == 'en' and probability.prob > min_prob:
            is_english = True
    
    return is_english


def main():
    poem_path = Path(r'english_poems.pickle')

    df = pd.read_pickle(poem_path)

    for i in range(len(df)):
        # removes junk from poems: newlines, punctuation, and widespaces
        poem = df.content[i].replace('\n', ' ')
        poem = poem.translate(str.maketrans('', '', string.punctuation))
        poem = re.sub('\s\s+' , ' ', poem)
        if detect_english(poem, .98) != True:
            df.drop(index=i, inplace=True)
    
    df.reset_index(drop=True, inplace=True)
    
    df.to_pickle('english_poems.pickle')

if __name__ == '__main__':
    main()

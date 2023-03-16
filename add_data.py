# this script is used to generate new poems from poems in the dataset
# usisng synonyms that arent in the dataset

# get current poems
# write new poems based on the first 2000
# only use synonyms that arent in the dataset, but their synonyms occur
# only on nouns
# word classification 


import pandas as pd
# pip install py_thesaurus
from py_thesaurus import Thesaurus

input_word = "dream"

new_instance = Thesaurus(input_word)

# Get the synonyms according to part of speech
# Default part of speech is noun

print(new_instance.get_synonym())



def get_poems(file_name: str) -> pd.DataFrame:
    with open(file_name, 'r'):
        pass # get poem data

def create_simmilar_poems(df: pd.DataFrame, num: int) -> pd.DataFrame:
    pass
    # write new poems into df on top and return the entire df

def main():
    df = get_poems('poems.pickle')

    df = create_simmilar_poems(df, 10)
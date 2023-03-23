import pandas as pd
import re
import contractions


pattern1 = re.compile('[&,.”‘-“;@:"\'„—#“‛-‟…?!‚’_)–(*)$]+')
pattern2 = re.compile('[^a-zA-Z0-9]')
pattern3 = re.compile('\s\s+')

def remove_punc(dirty_line) -> str:
    line = dirty_line.encode('ascii', 'ignore')
    line = line.decode()
    line = line.replace("'", '')
    line = re.sub(pattern1, ' ', line)
    line = line.replace('-', ' ')
    line = re.sub(pattern2, ' ', line)
    line = re.sub(pattern3, ' ', line)
    return line


def cleaner(text) -> list[str]:
    cleaned_poems = []
    for string in text:
        lines = string.split('\n')
        good_lines = ''

        for line in lines: 
            line = line.replace('\'', "'")
            line = line.lower() + ' NEWLINE '
            # replaces contractions with their expanded version: can't -> cannot
            line = contractions.fix(line)
            # removes punctuation from the text and makes words lowercase
            line = remove_punc(line)
            
            good_lines += line 

        # removes the ' NEWLINE ' from the end of the poem
        good_lines = re.sub(r'\s\s+', ' ', good_lines)
        cleaned_poems.append(good_lines[:len(good_lines)-9])
        
    return cleaned_poems


def main():
    df = pd.read_pickle('mostly_english_poems.pickle')
    print(len(df))

    df.content = cleaner(df.content)

    df.to_pickle('name_of_df.pickle')


if __name__ == '__main__':
    main()
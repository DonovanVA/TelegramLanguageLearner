from collections import Counter
import pandas as pd
from lib.nlp import is_english_word

def extractWordsFromText(arr, cleaned_df):
    """
    Extracts words from the 'text' column of a DataFrame and appends them to a given list.

    Parameters:
    arr (list): The list to which the extracted words will be appended.
    cleaned_df (pandas.DataFrame): The DataFrame containing the text data.

    Returns:
    None
    """
    user_words_df = cleaned_df[cleaned_df['user_id'] == cleaned_df['sender_id']]
    for words in user_words_df['text']:
        res = words.split()
        for word in res:
            arr.append(word)


def extractWordsIntoDF(array):
    """
    Extracts words from a given list and creates a DataFrame with word counts.

    Parameters:
    array (list): The list containing the words.

    Returns:
    pandas.DataFrame: A DataFrame with columns 'Word', 'Count', and 'isWord'.
                      'Word' represents the word extracted, 'Count' represents
                      the frequency of the word, and 'isWord' indicates whether
                      the word is an English word or not.
    """
    lowercase_words = [word.lower() for word in array]
    word_count = dict(Counter(lowercase_words))
    df = pd.DataFrame(list(word_count.items()), columns=['Word', 'Count'])
    
    is_word_list = []
    for word in df['Word']:
        is_word_list.append(is_english_word(word))
    df['isWord'] = is_word_list
    
    df = df.sort_values(by='Count', ascending=False)
    return df


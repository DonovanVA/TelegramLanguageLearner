import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import nltk
from nltk.corpus import words as nltk_words
from lib.pandas_database_functions import queryCSV, createReplaceCSV, jsonToDict
from lib.extractors import extractWordsFromText, extractWordsIntoDF
import asyncio
from lib.paths import get_prev_path
import os
async def main():
    nltk.download('words')
    datasets_folder = 'datasets'
    raw_messages_file_path = os.path.join(get_prev_path(__file__), datasets_folder, 'raw_messages.csv')
    words_file_path = os.path.join(get_prev_path(__file__), datasets_folder, 'words.csv')
    uncleaned_df = queryCSV(raw_messages_file_path)
    cleaned_df = uncleaned_df.dropna()
    uncleaned_df.reset_index(drop=True,inplace=True)
    words_arr=[]
    extractWordsFromText(words_arr,cleaned_df)
    words_df= extractWordsIntoDF(words_arr)
    createReplaceCSV(words_df,words_file_path)

asyncio.run(main())
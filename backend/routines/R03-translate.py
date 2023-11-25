import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import pandas as pd
import nltk
from nltk.corpus import words as nltk_words
from googletrans import Translator
from lib.pandas_database_functions import queryCSV,createReplaceCSV,jsonToDict # Import the specific function you need
from lib.nlp import translate_words,translate_word
import asyncio
from lib.paths import get_prev_path
async def main():
    nltk.download('words')
    translator = Translator()
    datasets_folder = 'datasets'
    translator_registry_folder = 'translator'
    words_file_path = os.path.join(get_prev_path(__file__), datasets_folder, 'words.csv')
    translated_words_file_path = os.path.join(get_prev_path(__file__), datasets_folder, 'words.csv')
    translator_registry_file_path = os.path.join(get_prev_path(__file__), translator_registry_folder, 'languages.json')
    new_words_df=queryCSV(words_file_path)
    language_dict = jsonToDict(translator_registry_file_path)
    new_words_df = new_words_df[new_words_df['isWord'] == True]
    new_words_df.reset_index(drop=True,inplace=True)
    ## remove the rows with empty 
    truncated_words_df = new_words_df.head(50)
    # Create a copy of the DataFrame
    truncated_words_df = truncated_words_df.copy()
    # Apply translation using .loc to avoid SettingWithCopyWarning
    lang_code ='ko'

    translations = truncated_words_df['Word'].apply(
        lambda x: translate_word(x, language_code=lang_code, translator=translator)
    )
    # Create separate columns for translation and pronunciation
    truncated_words_df[['Translation', 'Pronunciation']] = pd.DataFrame(translations.tolist(), index=truncated_words_df.index)
    truncated_words_df['language_code'] = lang_code
    truncated_words_df['language'] = truncated_words_df['language_code'].apply(lambda x: language_dict.get(x, 'Unknown'))
    createReplaceCSV(truncated_words_df,translated_words_file_path)
asyncio.run(main())
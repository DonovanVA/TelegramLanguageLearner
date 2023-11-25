import nltk
from nltk.corpus import words as nltk_words
nltk.download('words')
import pandas as pd
def is_english_word(word):
    """
    Check if a given word is an English word.

    Parameters:
    word (str): The word to be checked.

    Returns:
    bool: True if the word is an English word, False otherwise.
    """
    if set(word.lower()) <= set('ha'):
        return False
    return word.lower() in set(nltk_words.words())

def translate_word(text, language_code, translator):
    """
    Translate a word to the specified language.

    Parameters:
    text (str): The word to be translated.
    language_code (str): The language code of the target language.
    translator: The translator object used for translation.

    Returns:
    list: The translated word and pronunciation (or "NULL" if fields are missing).
    """
    try:
        translation = translator.translate(text, dest=language_code)
        translated_text = translation.text if hasattr(translation, 'text') else 'NULL'
        pronunciation = translation.pronunciation if hasattr(translation, 'pronunciation') else 'NULL'

        # Check if fields are missing and replace with "NULL"
        if translated_text == 'NULL' or pronunciation == 'NULL':
            translated_text = 'NULL'
            pronunciation = 'NULL'

        return [translated_text, pronunciation]
    except Exception as e:
        print(f"Translation error: {e}")
        return ['NULL', 'NULL']
# Function to translate words in a DataFrame column
def translate_words(column, language_code, translator):
    """
    Translate words in a DataFrame column to the specified language.

    Parameters:
    column (pandas.Series): The column containing words to be translated.
    language_code (str): The language code of the target language.
    translator: The translator object used for translation.

    Returns:
    pandas.DataFrame: DataFrame with translated words and their pronunciations.
    """
    translations = []
    for word in column:
        translation = translate_word(word, language_code=language_code, translator=translator)
        translations.append(translation)
    
    return translations
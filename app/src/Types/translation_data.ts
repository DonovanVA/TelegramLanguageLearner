export interface TranslationData {
  count: number;
  pronunciation: string;
  translation: string;
  word: string;
  isWord: boolean;
  language: string;
  language_code: string;
}

export interface RawTranslationData {
  data: TranslationData[];
  message: string;
}

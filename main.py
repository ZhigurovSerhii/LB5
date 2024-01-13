import locale
import string

class TextAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.locale = 'uk_UA.UTF-8'
        self._load_text()

    def _load_text(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.entire_text = file.read()
        except FileNotFoundError:
            print("Файл не знайдено.")
            exit(1)
        except Exception as e:
            print(f"Виникла помилка при читанні файлу: {e}")
            exit(1)

    def remove_punctuation_and_tokenize(self):
        text = self.entire_text.translate(str.maketrans('', '', string.punctuation))
        return text.split()

    def contains_ukrainian_and_english_words(self, words):
        ukrainian_words = any(any(char.isalpha() and ord(char) > 127 for char in word) for word in words)
        english_words = any(any(char.isalpha() and ord(char) <= 127 for char in word) for word in words)
        return ukrainian_words, english_words

    def get_sorted_words(self, is_ukrainian):
        filtered_words = [word for word in self.words if any(char.isalpha() and (ord(char) > 127) == is_ukrainian for char in word)]
        return sorted(filtered_words, key=locale.strxfrm)

    def analyze_text(self):
        self.words = self.remove_punctuation_and_tokenize()
        ukrainian_words, english_words = self.contains_ukrainian_and_english_words(self.words)

        print("\nСлова у тексті (відсортовані за алфавітом):")
        if ukrainian_words:
            ukrainian_sorted_words = self.get_sorted_words(True)
            print("\nУкраїнські слова:")
            for word in ukrainian_sorted_words:
                print(word)
        if english_words:
            english_sorted_words = self.get_sorted_words(False)
            print("\nАнглійські слова:")
            for word in english_sorted_words:
                print(word)

        print("\nЗагальна кількість слів у тексті:", len(self.words))


# Usage
filename = 'text.txt'
analyzer = TextAnalyzer(filename)
analyzer.analyze_text()

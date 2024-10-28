import string
from collections import Counter
from typing import List, Tuple, Dict


class TextFileAnalyzer:
    def __init__(self, file_path: str):
        self._file_path: str = file_path
        self._lines: List[str] = []
        self._words: List[str] = []
        self._word_count: int = 0
        self._line_count: int = 0
        self._unique_words_count: int = 0
        self._word_frequencies: Counter = Counter()

    def load_file(self) -> bool:
        """
        Loads the text file, reads its lines, and removes punctuation.
        :return: True if the file was successfully loaded, False otherwise.
        """
        try:
            with open(self._file_path, 'r', encoding='utf-8') as file:
                self._lines = file.readlines()
            self._line_count = len(self._lines)
            return True
        except FileNotFoundError:
            print(f"Error: The file '{self._file_path}' does not exist.")
            return False
        except IOError:
            print(f"Error: Could not read the file '{self._file_path}'.")
            return False

    def analyze_text(self) -> None:
        """
        Analyzes the text file content, calculating word count, unique words,
        and word frequencies. Processes text to exclude punctuation and whitespace.
        """
        if not self._lines:
            print("No content to analyze. Please ensure the file is loaded correctly.")
            return

        for line in self._lines:
            words = line.translate(str.maketrans('', '', string.punctuation)).split()
            self._words.extend([word.lower() for word in words if word.isalpha()])

        self._word_count = len(self._words)
        self._unique_words_count = len(set(self._words))
        self._word_frequencies = Counter(self._words)

    def get_word_count(self) -> int:
        """Returns the total word count."""
        return self._word_count

    def get_line_count(self) -> int:
        """Returns the total line count."""
        return self._line_count

    @property
    def get_unique_word_count(self) -> int:
        """Returns the count of unique words."""
        return self._unique_words_count

    def get_most_frequent_words(self, top_n: int = 5) -> List[Tuple[str, int]]:
        """
        Returns the top N most frequent words and their counts.
        :param top_n: Number of top frequent words to return.
        :return: A list of tuples with the word and its frequency.
        """
        if top_n < 1:
            print("Error: 'top_n' must be at least 1.")
            return []
        return self._word_frequencies.most_common(top_n)

    def get_word_frequency_percentage(self) -> Dict[str, float]:
        """
        Calculates the percentage of each word's occurrence in the file.
        :return: A dictionary with words as keys and percentage as values.
        """
        total_words = self._word_count
        if total_words == 0:
            print("No words to calculate percentages for.")
            return {}
        return {word: (count / total_words) * 100 for word, count in self._word_frequencies.items()}

    def display_report(self, top_n: int = 5) -> None:
        """
        Displays the analysis report with word count, line count, unique words,
        most frequent words, and word frequency percentages.
        """
        print("\nText File Analysis Report:")
        print(f"Total Words: {self.get_word_count()}")
        print(f"Total Lines: {self.get_line_count()}")
        print(f"Unique Words: {self.get_unique_word_count}")

        print(f"\nTop {top_n} Most Frequent Words:")
        for word, freq in self.get_most_frequent_words(top_n):
            print(f"'{word}': {freq} times")

        print("\nWord Frequency Percentages:")
        for word, percent in self.get_word_frequency_percentage().items():
            print(f"'{word}': {percent:.2f}%")

def main() -> None:
    file_path = input("Enter the path to the text file: ").strip()
    analyzer = TextFileAnalyzer(file_path)

    if not analyzer.load_file():
        return

    analyzer.analyze_text()
    top_n = input("Enter the number of top frequent words to display: ").strip()

    try:
        top_n = int(top_n)
        if top_n < 1:
            raise ValueError
    except ValueError:
        print("Invalid input for top N. Defaulting to top 5 frequent words.")
        top_n = 5

    analyzer.display_report(top_n=top_n)



if __name__ == "__main__":
    main()

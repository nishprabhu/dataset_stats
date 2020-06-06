""" Class containing methods required to get dataset statistics. """

from collections import Counter
import string
import pandas as pd
import seaborn as sns


class Stats:
    """ Stats Class """

    def __init__(self, filename):
        self.filename = filename

        # Data Statistics
        self.num_samples = 0
        self.num_words = 0
        self.num_characters = 0
        self.word_counts = Counter()
        self.num_punctuation = 0

        # Length histogram data
        self.words_per_sample = []
        self.characters_per_word = []

        # Aggregated statistics
        self.dataframe = None

    def compute_statistics(self):
        """ Compute statistics for the given file """
        with open(self.filename, "r") as file:
            for sample in file:
                self.process_sample(sample)
        self.get_dataframe()

    def process_sample(self, sample):
        """ Compute statistics for a single sample  """
        self.num_samples += 1
        words = sample.split(" ")
        num_words = len(words)
        self.num_words += num_words
        self.words_per_sample.append(num_words)
        self.word_counts.update(words)
        for word in words:
            self.process_word(word)

    def process_word(self, word):
        """ Compute statistics for a single word """
        num_characters = len(word)
        self.num_characters += num_characters
        self.characters_per_word.append(num_characters)
        for character in word:
            if character in string.punctuation:
                self.num_punctuation += 1

    def get_dataframe(self):
        """ Return dataset statistics as a dataframe """
        average_words_per_sample = self.num_words / self.num_samples
        average_characters_per_word = self.num_characters / self.num_words
        num_unique_words = len(self.word_counts)
        percentage_of_punctuation = self.num_punctuation / self.num_characters
        column_1 = [
            "Number of samples",
            "Average words per sample",
            "Average characters per word",
            "Number of unique words",
            "Percentage of punctuation",
        ]
        column_2 = [
            self.num_samples,
            average_words_per_sample,
            average_characters_per_word,
            num_unique_words,
            percentage_of_punctuation,
        ]
        data_dict = {"column_1": column_1, "column_2": column_2}
        self.dataframe = pd.DataFrame(data_dict)

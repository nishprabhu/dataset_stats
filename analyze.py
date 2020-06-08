""" Analyze the given dataset """

import os
import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from stats import Stats


class Statistics:
    """ Class to save statistics in LaTex tables and histograms to png. """

    def __init__(self, dataset_path, output_folder):
        # Set paths
        self.dataset_path = dataset_path
        self.tables_path = os.path.join(output_folder, "tables")
        self.histograms_path = os.path.join(output_folder, "histograms")

        # Create directories
        Path(self.tables_path).mkdir(parents=True, exist_ok=True)
        Path(self.histograms_path).mkdir(parents=True, exist_ok=True)

        # Statistics
        self.name = None
        self.dataframes = []
        self.ax_words = "words"
        self.ax_characters = "characters"

        if os.path.isdir(self.dataset_path):
            self.process_folder(self.dataset_path)
        else:
            self.process_file(self.dataset_path)

        # Save to disk
        self.save_to_latex()
        self.save_plots()

    def process_folder(self, path):
        """ Process all the files in the given folder """
        filenames = os.listdir(path)
        for filename in filenames:
            self.process_file(os.path.join(path, filename))

    def process_file(self, path):
        """ Process a single file """
        filename = os.path.basename(path)
        self.name, ext = os.path.splitext(filename)
        label = ext[1:].title()

        # Get statistics
        file_stats = Stats(path)
        file_stats.compute_statistics()

        file_stats.dataframe.columns = ["", label]
        self.dataframes.append(file_stats.dataframe)

        # Plot histograms
        plt.figure(self.ax_words)
        axlabel = "Number of words"
        sns.distplot(file_stats.words_per_sample, axlabel=axlabel, label=label)

        plt.figure(self.ax_characters)
        axlabel = "Number of characters"
        sns.distplot(file_stats.characters_per_word, axlabel=axlabel, label=label)

    def save_to_latex(self):
        """ Save the computed statistics to a .tex file """
        dataframe = pd.concat(self.dataframes, axis=1).T.drop_duplicates().T
        print(dataframe)
        caption = "Statistics of the {} dataset".format(self.name)
        label = "tab:{}_stats".format(self.name)
        save_path = os.path.join(self.tables_path, self.name + ".tex")
        dataframe.to_latex(
            save_path,
            header=True,
            index=False,
            # float_format="%.2f",
            caption=caption,
            label=label,
            na_rep="-",
        )

    def save_plots(self):
        """ Save plots to disk """
        plt.figure(self.ax_words)
        plt.title("Histogram of the number of words per sample")
        plt.legend()
        save_path = os.path.join(self.histograms_path, self.name + "_words.png")
        plt.savefig(save_path)

        plt.figure(self.ax_characters)
        plt.title("Histogram of the number of characters per word")
        plt.legend()
        save_path = os.path.join(self.histograms_path, self.name + "_characters.png")
        plt.savefig(save_path)


def main():
    """ Main Function """
    parser = argparse.ArgumentParser(description="Analyze the given dataset")
    parser.add_argument("--dataset_path", help="Path to dataset", required=True)
    parser.add_argument(
        "--output_folder", default="outputs", help="Folder to save dataset statistics",
    )
    args = parser.parse_args()

    sns.set()

    statistics = Statistics(args.dataset_path, args.output_folder)


if __name__ == "__main__":
    main()

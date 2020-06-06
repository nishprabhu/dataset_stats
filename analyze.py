""" Analyze the given dataset """

import os
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
from stats import Stats


def get_stats_and_histograms(path, ax_words, ax_characters):
    """ Get histograms and LaTex tables containing dataset statistics """
    filename = os.path.basename(path)
    file_stats = Stats(path)
    file_stats.compute_statistics()

    # Save LaTex tables
    caption = "Statistics of {} dataset".format(filename)
    label = "tab:{}_stats".format(filename)
    file_stats.dataframe.to_latex(
        filename + ".tex",
        header=False,
        index=False,
        float_format="%.2f",
        caption=caption,
        label=label,
    )

    # Plot the histograms
    label = os.path.splitext(filename)[-1].split(".")[-1]
    plt.figure(ax_words)
    axlabel = "Number of words"
    sns.distplot(file_stats.words_per_sample, axlabel=axlabel, label=label)
    plt.figure(ax_characters)
    axlabel = "Number of characters"
    sns.distplot(file_stats.characters_per_word, axlabel=axlabel, label=label)


def plot(ax_words, ax_characters, filename=""):
    """ Plot histograms """
    plt.figure(ax_words)
    plt.title("Histogram of the number of words per sample")
    plt.legend()
    plt.savefig("{}_words.png".format(filename))

    plt.figure(ax_characters)
    plt.title("Histogram of the number of characters per word")
    plt.legend()
    plt.savefig("{}_characters.png".format(filename))


def main():
    """ Main Function """
    parser = argparse.ArgumentParser(description="Analyze the given dataset")
    parser.add_argument("--path", help="Path to dataset", required=True)
    args = parser.parse_args()

    ax_words = "words"
    ax_characters = "characters"
    if os.path.isdir(args.path):
        filenames = os.listdir(args.path)
        for filename in filenames:
            path = os.path.join(args.path, filename)
            get_stats_and_histograms(path, ax_words, ax_characters)
        name, _ = os.path.splitext(filename)
        plot(ax_words, ax_characters, filename=name)
    else:
        filename = os.path.basename(args.path)
        get_stats_and_histograms(args.path, ax_words, ax_characters)
        plot(ax_words, ax_characters, filename=filename)


if __name__ == "__main__":
    main()

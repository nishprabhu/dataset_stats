""" Analyze the given dataset """

import os
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
from stats import Stats


def get_stats_and_histograms(path):
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
    plt.figure("words")
    ax_words_per_sample = sns.distplot(file_stats.words_per_sample)
    plt.figure("characters")
    ax_characters_per_word = sns.distplot(file_stats.characters_per_word)
    return ax_words_per_sample, ax_characters_per_word


def plot(ax_words, ax_characters, filename=""):
    """ Plot histograms """
    plt.figure("words")
    plt.savefig("{}_words.png".format(filename))

    plt.figure("characters")
    plt.savefig("{}_characters.png".format(filename))


def main():
    """ Main Function """
    parser = argparse.ArgumentParser(description="Analyze the given dataset")
    parser.add_argument("--path", help="Path to dataset", required=True)
    args = parser.parse_args()

    if os.path.isdir(args.path):
        filenames = os.listdir(args.path)
        for filename in filenames:
            path = os.path.join(args.path, filename)
            ax_words, ax_characters = get_stats_and_histograms(path)
        name, _ = os.path.splitext(filename)
        plot(ax_words, ax_characters, filename=name)
    else:
        filename = os.path.basename(args.path)
        ax_words, ax_characters = get_stats_and_histograms(args.path)
        plot(ax_words, ax_characters, filename=filename)


if __name__ == "__main__":
    main()

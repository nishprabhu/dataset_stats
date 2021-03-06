# Dataset Stats

Code to analyze a dataset and save dataset statistics and plot relevant histograms. The statistics are saved in a .tex file for easy import to your LaTex project.

## Statistics Computed:
* Number of samples
* Least number of words per sample
* Average number of words per sample
* Most number of words per sample
* Least number of characters per word
* Average number of characters per word
* Most number of characters per word
* Number of unique words (vocabulary size)
* Percentage of characters that are punctuation

Other stats like total number of words, total number of characters etc. are computed, but are not saved to disk as they are not as informative. Extend the Stats class to save other statistics.

## Histograms saved:
* Histogram of number of words per sample
* Histogram of number of characters per word

## To analyze a dataset, run:
```bash
python analyze.py --dataset_path <path_to_dataset_file_or_folder> --output_folder <path_to_output_folder>
```

The --dataset_path argument takes either a file path or a folder path. If a file is passed, then the statistics for that file are computed and saved as a .tex file. The histograms are also plotted and saved. 
--dataset_path should only point to a folder if the folder contains two files of the same dataset, i.e. the source and target files for sequence-to-sequence tasks. In this case, the statistics of the two files are saved in the same table, and the histograms are plotted in the same figure. 
All outputs are saved in the path provided via --output_folder. If no path is provided, then outputs are saved in the current directory.

The input dataset files should be named with the source/target information in the extensions. For example, for the wmt machine translation dataset, the files containing the German and English sentences should be named as follows:
* wmt.german
* wmt.english

from tools import datasets
from tools.datasets import *

if __name__ == '__main__':
    # download data from kaggle
    datasets.download_data()

    # preprocess the csv
    datasets.preprocessing()
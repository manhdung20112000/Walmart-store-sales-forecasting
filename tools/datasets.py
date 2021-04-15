import os
import pandas as pd
import requests
from zipfile import ZipFile

from model.configs import *


def download_data():
    url = [FEATURES_URL, STORES_URL, TRAIN_URL, TEST_URL]
    names = ['feature.csv.zip', 'stores.csv', 'train.csv.zip', 'test.csv.zip']

    try: 
        os.mkdir(DATA_PATH) 
    except OSError as error: 
        print('Dir created!')  
    os.chdir(DATA_PATH)

    for idx in range(len(url)):
        r = requests.get(url[idx], allow_redirects=True)
        print(f"Downloading {names[idx]} . . .")
        # open(DATA_PATH+names[idx], 'wb').write(r.content)
        with open(names[idx], 'wb') as f:
            f.write(r.content)

    for idx in range(len(url)):
        if names[idx][-3:] == 'zip':
            with ZipFile(names[idx], 'r') as zip:
                # extracting all the files
                print(f'Extracting all the file {names[idx]}...')
                zip.extractall()

            os.remove(names[idx])
        
    print("All done!")

def preprocessing():
    # cd data
    os.chdir(DATA_PATH)

    # read cvs file
    features    = pd.read_csv('features.csv')
    stores      = pd.read_csv('stores.csv')
    train       = pd.read_csv('train.csv')
    test        = pd.read_csv('test.csv')

    # join stores with features 
    features_joined = features.merge(stores, how='inner', on='Store')

    print('Save to csv')
    features_joined.to_csv('features_join.csv', index=False)

    print(features_joined.head(10))
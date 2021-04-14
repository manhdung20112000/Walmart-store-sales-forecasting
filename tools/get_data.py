import requests
from zipfile import ZipFile
import os

DATA_PATH = 'data/'

feature_url = 'https://storage.googleapis.com/kagglesdsdata/competitions/3816/32105/features.csv.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1618676306&Signature=R73EWrFWNIa3mgs8WvUjT1qRyH8GuArbib%2BoGQIB8%2FYyCLCyZKQsncyukl4DJPytsg%2BPaS%2F%2BLolLFWHV6JB7877pvou0xr9dF%2Bl%2BCHIHws752glTS8KPy4heNAPI6C4lfLMpdqKNSg7Y6z%2BAHHlamj26OKYl02nxZr4DSS2WGLEJ6ZoVsRGyQOTHPy64oasLnnWF9Bqj1IoJFfds12LPABS2HnhCIrj7leNHcm8kAsE%2FYJYRmYoCd%2BEX4uWfyTrTL1Ueuu%2F%2BJM5borAHGAI2WauR3Xu9dTgNXskL2U30Ke7to85%2BFSii%2FbOMtGPFj%2F8SdA9O9AVRadGcUIwixDTqrA%3D%3D&response-content-disposition=attachment%3B+filename%3Dfeatures.csv.zip'
store_url   = 'https://storage.googleapis.com/kagglesdsdata/competitions/3816/32105/stores.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1618676542&Signature=n8lRDxNpTTbAoDTjLeoiqKPD3j2Cu4%2FyEUoar0vYeNlbN6DFeTKnSI8qpDtXF4sjqSM%2BOGEwWpytxElX%2BB6p%2F2L6LoDL5dmwGDTpmzPdrY%2BE3VdlWQ5SsvBULM6UuX53iGUUwIivltL0gsZB1ViPQmDoYHalO6MwMbp4wGmb7YpzEfmb9Se%2FRCyDKoUOhGZkEhxcJox%2BS5du8bmIYDUHPB%2BvjiAPV5QIaZe0O8JJyHkOa%2BdBbbE%2B%2B3N%2FF88p0aLXZnMXKdhVDIjg27pG4tfb84rmoQ7v8aylSDJkjm4mRig3J%2BzWyqd45yd6rJYzF0KBYvXJnGQSf2cFrtRTZMMrzg%3D%3D&response-content-disposition=attachment%3B+filename%3Dstores.csv'
train_url   = 'https://storage.googleapis.com/kagglesdsdata/competitions/3816/32105/train.csv.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1618676578&Signature=nVIOEu2AC%2FFTqUK4kaqGUD186FEMlpb0K3qH3BDroCsZBFOzfwtPAEHzQwR%2BSXdnF2LxAKHcKdXjBVWZ60t70g8q34ou%2Bc%2BFweYNMI9EVguR8Px9dNrwVi0jvmco7nJbo14lf0V%2BbvnvnZ2WAI9B6TcAxG0lpkdMBva5TQSkjFavwcwfA8Qt6bmDPf34u%2FCk0xBxP%2B614t5gGhyNR16BVN56SQcCdSgeMcFl5AWuME%2FCSdF2slBi6fyp2redKd6KBKGilwz%2B27h%2FyAwXocm%2BLuz%2FnOoNLWIPcM7cwXRtAkL1VOoS2JINK5Tl%2BN0SrItfRyytnjJBToSF4eGkQVmaww%3D%3D&response-content-disposition=attachment%3B+filename%3Dtrain.csv.zip'
test_url    = 'https://storage.googleapis.com/kagglesdsdata/competitions/3816/32105/test.csv.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1618676571&Signature=UxQaBWix3Bm%2BNHGp5czNd4RTOThQM4wyeissG44%2F63e9xNW6xp0xL5Xe2KK%2FCAcHYwwop0okQJ3MQhbiIZrUaOOxTEy0bpa%2FOAeAGJWCntysKW6vOT2U4pNZ7b%2FZF8kIvBe72zXaL7neEHrj6%2F26wyWxVpZi4ZB7tVER1nneuI57Ex6GzMB0%2FrLdhz3vuauerulIwdq3sPum5CqI%2FKfdQQutV%2FDfuwrgYczLrfwNqzxZn%2FdGnVvjzaj1k5noxPSmtTS0AnJKeemfbpCqODyfjmBRMZtet8JzYh3AXY0XVGWuCn0msaSPBEKFS0oNYIS65NJLCUtlpqqG6M2jrgVZ9A%3D%3D&response-content-disposition=attachment%3B+filename%3Dtest.csv.zip'

url = [feature_url, store_url, train_url, test_url]
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




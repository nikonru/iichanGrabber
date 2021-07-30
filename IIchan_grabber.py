import os

import requests
from bs4 import BeautifulSoup

import argparse
from tqdm import tqdm

#command line interface
p = argparse.ArgumentParser()

p.add_argument("file")

p.add_argument("-d","--dir_name", default = "img")
p.add_argument("-w","--wrapper_name", default = "")

args = p.parse_args()

#arguments
DIR_NAME = args.dir_name

FILE_NAME = args.file

WRAPPER_NAME = args.wrapper_name

#parsing HTML
with open(FILE_NAME, "r" ,encoding='utf-8') as file:

    content = file.read()
    soup = BeautifulSoup(content, "lxml")

    img = soup.find_all("a", class_="imglink")

    i = 0

    try:
        os.makedirs(DIR_NAME)
    except:
        print("Directory alredy exsists, continue? Y/N")

        answer = input()
        answer = answer.lower()

        if answer == "y":
            pass
        elif answer == "n":
            exit(-1)

    for picture in tqdm(img):

        url = str(picture["href"])

        #getting file extension
        ext = url[::-1]
        ext = ext.split(".")[0]
        ext = ext[::-1]

        index = "["+str(i)+"]"

        file = open(DIR_NAME + "/" + WRAPPER_NAME + index + "." + ext, 'wb')

        try:
            image = requests.get(url).content
        except:
            print("Error occured when loading from address " + url)
            pass

        file.write(image)
        file.close()

        i += 1



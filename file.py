#!/usr/bin/env/ python

#1. load a datas set from a file
#2. "organize" that file. so we can access colums *or* rows of ti easily
#3. copmute some "summary statics" about the dataset
#4. print those summary statistics


#1. load a data set
#1a. accept arbitrary filename as argument
#1b. load the file

#1a
from argparse import ArgumentParser

parser = ArgumentParser(description='A CSV reader + stats maker')
parser.add_argument('csvfile',
               help='Path to the input csv file.')

parsed_args = parser.parse_args()
print(parsed_args)
print(parsed_args.csvfile)


my_csv_file = parsed_args.csvfile

import os

#if os.path.isfile(my_csv_file):
#  print("yay, it's real!!")
#else:
#  print('ooops, plz give rl file')


assert(os.path.isfile(my_csv_file))
print('hello')



# 1b. load the file
import pandas as pd

data = pd.read_csv(my_csv_file, sep='\s+|,', header=None)
print(data.head())

# for item in dir(data):
#   print(item)

print(data.shape)

print



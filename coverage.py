import argparse
import os
import shutil
import csv


def parse_args():
    """Specify a parser for a single mandatory command-line argument"""
    parser = argparse.ArgumentParser(description='generate coverage analysis of measurement data CSVs produced by data-extract.py')
    parser.add_argument('data_path', help='path to a single device\'s CSV data dump')
    parser.add_argument('-o', '--out_path', help='path to the output directory, defaults to data/analysis')

    return parser.parse_args()


def count_rows():
    print('Rows')


def count_cols():
    print('Cols')


#Check if at least one CSV file exists in data_path
def hasCSV():
    file_list = os.listdir(data_path)
    csvlist = csv_list(file_list)
    return len(csvlist) > 0


#Returns a list of the csv files in the director file_list
def csv_list(file_list):
    extension = '.csv'
    return [file for file in file_list if file.lower().endswith(extension)]



def process_csv(csvfile):
    print('Filename: ' + csvfile)
    print('    Number of Colums: ')
    print('    Number of Rows: ')




args = parse_args()
data_path = args.data_path
out_path = args.out_path if args.out_path is not None else os.path.join(data_path, 'analysis')


is_folder = os.path.isdir(data_path)
has_csv = hasCSV()
is_valid = is_folder and has_csv


if not os.path.exists(out_path):
    os.makedirs(out_path)


if is_valid:
    file_list = os.listdir(data_path)
    for csvfile in csv_list(file_list):
        process_csv(csvfile)

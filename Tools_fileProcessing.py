# filename: Tools.fileProcessing.py
import urllib
import csv
import pandas


def get_csv_file_row_number(csv_file_name):  # not include first row
    DataFrame = pandas.read_csv(csv_file_name)
    return len(DataFrame)


def add_column_to_csv(csv_file_name, new_column_title, new_column_content_list):
    DataFrame = pandas.read_csv(csv_file_name)
    DataFrame[new_column_title] = new_column_content_list
    DataFrame.to_csv(csv_file_name)


def download_link(url, filename):
    print "downloading " + filename
    urllib.urlretrieve(url, filename)
    print filename + " downloaded"


def download_from_csv(csv_file_name, url_row, filename_row):
    csv_file = file(csv_file_name, 'rb')
    csv_reader = csv.DictReader(csv_file)
    for file_info in csv_reader:
        download_link(file_info[url_row], file_info[filename_row])
    csv_file.close()

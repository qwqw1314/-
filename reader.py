import csv

def filereader():
    file1 = open('data/polarity.csv', 'r', encoding = 'utf-8')
    polarity = csv.DictReader(file1)
    file2 = open('data/intensity.csv', 'r', encoding='utf-8')
    intensity = csv.DictReader(file2)
    file3 = open('data/expressive-type.csv', 'r', encoding='utf-8')
    express = csv.DictReader(file3)
    return polarity, intensity, express
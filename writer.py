import csv

file = open('data/polarity.csv', 'r', encoding = 'utf-8')
dictreader = csv.DictReader(file)

with open('data/polarity2.csv', 'w', encoding='utf-8') as file2:
    fieldnames = ['ngram', 'freq', 'COMP', 'NEG', 'NEUT', 'None','POS', 'max.value', 'max.prop']
    dictwriter = csv.DictWriter(file2, fieldnames=fieldnames)
    dictwriter.writeheader()
    for line in dictreader:
        arr = []
        for ngram in line['ngram'].split(';'):
            temp = ngram.split('/')
            arr.append(temp[0])
        line['ngram'] = "/".join(arr)
        dictwriter.writerow(line)
import csv
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


mystring = ''
# thislist = []
train = []
with open('Book1.csv', 'rt')as f:
    data = csv.reader(f)
    i = 1
    for row in data:
        x = str(row[5])+" "+str(row[8])+" "+str(row[7])
        y = row[2]

        train.append((x, y))
        if i == 20:
            break
        i = i + 1

cl = NaiveBayesClassifier(train)

# Classify some text

# Input sample - Weight Gender Age
print(cl.classify("60 Male 27"))


exit()
import csv
import sys

def read_words(f):
    words = []

    for line in f:
        for word in line.split(' '):
            word = word.strip(".,?!-\'\"()[]:;\n").lower()
            if word != '':
                words.append(word)
    return words

def count_frequencies(words):
    freqs = {}

    for word in words:
        if word not in freqs:
            freqs[word] = 1
        else:
            freqs[word] += 1

    return freqs

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: wordcount.py inputfile.txt outputfile.txt")
        sys.exit(-1)

    f = open(sys.argv[1])
    words = read_words(f)
    frequencies = count_frequencies(words)
    f.close()

    f = open(sys.argv[2], "w")
    wtr = csv.writer(f)
    rows = frequencies.items()
    rows.sort(reverse=True, key = lambda tup: tup[1])
    wtr.writerows(rows)
    f.close()

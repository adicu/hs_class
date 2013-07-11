import sys
import json
import csv

def main():
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " input.csv output.json")
        sys.exit(1)

    jsonf = open(sys.argv[1], "r")
    csvf = open(sys.argv[2], "w")

    table = list(json.load(jsonf))

    wtr = csv.writer(csvf)

    for row in table:
        csvrow = []

        for cell in row:
            csvrow.append(str(cell))

        wtr.writerow(csvrow)

    jsonf.close()
    csvf.close()

main()

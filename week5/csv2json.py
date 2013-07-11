import csv
import json
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " input.csv output.json")
        sys.exit(1)

    csvf = open(sys.argv[1], "r")
    jsonf = open(sys.argv[2], "w")

    table = []

    for row in csv.reader(csvf):
        table.append(row)

    json.dump(table, jsonf)

    csvf.close()
    jsonf.close()

main()

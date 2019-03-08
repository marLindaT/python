import re
import csv

with open("workingSheet.csv", "r") as csv_input_file:
  inputFile = csv.reader(csv_input_file, delimiter = ",")
  for row in inputFile:
    print(row)

import csv
import re


class OilStrain:
  inputFile = "workOrders.csv"

  def __init__(self):
    self.oilStrain = str(input("what oil Lot"))

  def getWorkOrderList(self):
    self.woType = []
    with open(self.inputFile, "r") as sourceFile:
      csv_reader = csv.reader(sourceFile, delimiter =",")
      
      for line in csv_reader:
        if line[5] == self.oilStrain and line[1] not in self.woType:
          self.woType.append(line[1])

    


    

    
test = OilStrain()

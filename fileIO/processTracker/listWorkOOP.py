import csv
import re


class OilStrain:
  inputFile = "workOrders.csv"

  def __init__(self):
    self.oilStrain ="Oil Black Widow" # str(input("what oil Lot"))

  def getWorkOrderList(self):
    "search and make list of all work orders done for an Oil Productn type"
    self.woType = []
    with open(self.inputFile, "r") as sourceFile:
      csv_reader = csv.reader(sourceFile, delimiter =",")
      
      for line in csv_reader:
        if line[5] == self.oilStrain and line[1] not in self.woType:
          
          self.woType.append(line[1])#store list of Work orders here
          
    return self.woType

  def getOilLotCodes(self):
    "collect all lot numbers of a given oil production into a list"
    self.lotList = []
    with open(self.inputFile, "r") as sourceFile:
      csv_reader = csv.reader(sourceFile, delimiter =",")
      for line in csv_reader:
        if line[5] == self.oilStrain and len(line[3])<8:
          m = re.match(r"^\d{4}(?!\d)", line[3])
          n = re.match(r"^\d{3}(?!/d)", line[3])
          if m!= None:
            if m.group() not in self.lotList:
              self.lotList.append(m.group())
          if n!= None:
            if n.group() not in self.lotList:
              self.lotList.append(n.group())
      self.lotList.sort()  
    
    return self.lotList


  def getInput(self):
    "given a list of lot numbers return "
    with open(self.inputFile, "r") as sourceFile:
      file = csv.reader(sourceFile, delimiter=',')
      
      self.inputList = []     

      for line in file:
        for item in self.lotList:
          for wo in self.woType:
            
            

##            if len(item)==4:
##              
##              m = re.match(r"^\d{4}(?!\d)", line[3])
##              if m:
##                if line[3] == item and line[1]==wo:
##                  
##                  self.inputList.append([line[3], line[6]])
##                  
            if len(item) ==3:
              n = re.match(r"^\d{3}(?!\d)", line[3])
              if n:
                if line[1]==wo:
                  self.inputList.append([item, line[6]])
                
    return self.inputList







# instantiate and call

test = OilStrain()

test.getWorkOrderList()

test.getOilLotCodes()

print(test.lotList)

test.getInput()

print(test.inputList)



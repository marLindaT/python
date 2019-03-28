import csv
import re


## inputFile = str(input("What is the input file?:"))
##saveFile = str(input("What do you want to name your output file?:"))

##user enter oil type as defined in Ample W/O "Production" column
##Oil Black Widow
##Oil Jesus OG
##Oil Sativa Blend
##etc....
def queryOilStrain():
  "get input oil strain type"
  lotType = str(input("What lot/strain type?:"))

  return lotType

result={}

#create a list of all WO Types
def getWOList(inputFile="workOrders", lotType="Oil Black Widow"):

  with open(inputFile+".csv", "r") as sourceFile:
    csv_reader = csv.reader(sourceFile, delimiter =",")
    woType = []
    for line in csv_reader:
      if line[5] == lotType and line[1] not in woType:
        woType.append(line[1])
        
  return woType

result["Work Orders Completed"] = getWOList()
    
##put all oil lots into a list
def getOilLotCodes(inputFile="workOrders", lotType="Oil Black Widow"):
  "collect all lot numbers of a given oil production into a list"
  
  with open(inputFile+".csv", "r") as sourceFile:
    csv_reader = csv.reader(sourceFile, delimiter=',')
    lotList = []
    for line in csv_reader:
      if line[5] == lotType and len(line[3])<8:
               
        ## find lot numbers of len 4
        m = re.match(r"^\d{4}(?!\d)", line[3])
        if m!= None:
          if m.group() not in lotList:
            lotList.append(m.group())
        ## find lot numbers of len 3     
        n = re.match(r"^\d{3}(?!/d)", line[3])
        if n!= None:
          if n.group() not in lotList:
            lotList.append(n.group())
  lotList.sort()  
  
  return lotList

lotList = getOilLotCodes()
print("LOT LIST BELOW")
print(lotList)

result["Lot List"] = getOilLotCodes()

def getAllInputs(result = result, inputFile="workOrders",):
  ""

  with open(inputFile+".csv", "r") as sourceFile:
    file = csv.reader(sourceFile, delimiter=',')

    for order in result["Work Orders Completed"]:
      getInput(workOrderType = order)





  return None


def getInput(inputFile="workOrders", lotList = lotList, workOrderType="Oil - Milling"):
  "given a list of lot numbers return a list of equal len/order of input mass in grams"
  with open(inputFile+".csv", "r") as sourceFile:
    file = csv.reader(sourceFile, delimiter=',')
    
    inputList = []
    holdingVar = 0

    for line in file:
      for item in lotList:

        if len(item)==4:
          m = re.match(r"^\d{4}(?!\d)", line[3])
          if m:
            if line[3] == item and line[1]==workOrderType:
              inputList.append([line[3], line[6]])
              
        if len(item) ==3:
          n = re.match(r"^\d{3}(?!\d)", line[3])
          if n:
            
            if line[3] == item and line[1]==workOrderType:

              inputList.append([line[3], line[6]])
            
  result[workOrderType] = inputList
                
  return inputList

 
    

    

    


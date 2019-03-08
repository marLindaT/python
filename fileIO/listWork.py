import csv
import re


## inputFile = str(input("What is the input file?:"))
##saveFile = str(input("What do you want to name your output file?:"))

##user enter oil type as defined in Ample W/O "Production" column
##Oil Black Widow
##Oil Jesus OG
##Oil Sativa Blend
##etc....


    
## (?!foo)	Negative Lookahead	Asserts that what
##immediately follows the current position in the string is not foo
    
##put all oil lots into a list
def getOilLotCodes(inputFile="workOrders"):
  "collect all lot numbers of a given oil production into a list"
  lotType = str(input("What lot/strain type?:"))
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


def getInput(inputFile="workOrders", lotList=lotList, workOrderType="Oil - Milling"):
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
              holdingVar += float(line[6])
              print("yes")
          
         
          
             
  return inputList

print(getInput())
    
      

    

    



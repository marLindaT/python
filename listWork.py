import csv
import re


## inputFile = str(input("What is the input file?:"))
##saveFile = str(input("What do you want to name your output file?:"))

##user enter oil type as defined in Ample W/O "Production" column
##Oil Black Widow
##Oil Jesus OG
##Oil Sativa Blend
##etc....


    

    
##put all oil lots into a list
def getOilLotCodes(inputFile="workOrders"):
  "collect all lot numbers of a given oil production into a list"
  lotType = 'Oil Black Widow'
##  lotType = str(input("What lot/strain type?:"))
  with open(inputFile+".csv", "r") as sourceFile:
    csv_reader = csv.reader(sourceFile, delimiter=',')
    lotList = []
    for line in csv_reader:
      if line[5] == lotType and len(line[3])<8:
      	
      	q = re.search(r"^\d{4}(?!\d)", line[3])
      	if q != None:
      		if q.group() not in lotList:
      			lotList.append(q.group())
      		
      	q =re.search(r"^\d{3}(?!\d)", line[3])
      	if q != None:
      		if q.group() not in lotList:
      			lotList.append(q.group())
    for i in lotList:
    	float(i)
    
    lotList.sort()         
  return lotList

lotList = getOilLotCodes()
print("LOT LIST BELOW")
print(lotList)


def getWOInput(inputFile="workOrders", lotList=lotList, workOrderType="Oil - Milling"):
  "given a list of lot numbers return a list of equal len/order of input mass in grams"
  
  with open(inputFile+".csv", "r") as sourceFile:
    csv_reader = csv.reader(sourceFile, delimiter=',')
    inputList = []
    
    
                                  
  return None

print(getWOInput())
    
      

    

    



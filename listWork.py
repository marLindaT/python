import csv


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
  lotType = str(input("What lot/strain type?:"))
  with open(inputFile+".csv", "r") as sourceFile:
    csv_reader = csv.reader(sourceFile, delimiter=',')
    lotList = []
    for line in csv_reader:
      if line[5] == lotType and len(line[3])<7:
        if line[3] not in lotList:
          lotList.append(line[3])
    
  return lotList

print(getOilLotCodes())
      

    

    



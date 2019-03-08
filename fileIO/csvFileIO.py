import csv

saveFile = str(input("What do you want to name your output file?:"))

##user enter oil type as defined in Ample W/O "Production" column
##Oil Black Widow
##Oil Jesus OG
##Oil Sativa Blend
##etc....
oilType = str(input("What oil lot type do you want to look at?:"))

## open original file
with open("workOrders.csv", "r") as sourceFile:
## use csv.reader() method
    csv_reader = csv.reader(sourceFile, delimiter=',')

##open new file
    with open(saveFile+".csv", "w") as newFile:
## use csv.writer() method
      csv_writer = csv.writer(newFile, delimiter=",")

##check every row in sourceFile
      for line in sourceFile:
        if 

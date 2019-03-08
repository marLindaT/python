import re
import csv



arr = ["1","2","333","444","555","(667)","(4321)","(897)-1", "apple"]
strin = "(338)h"

with open("workOrders.csv", "r") as sourceFile:
    csv_reader = csv.reader(sourceFile, delimiter=',')
    lotList = []
    for line in csv_reader:
      x=0
      while x<100:
        lotList.append(line[3])
        x+=1
    print(lotList)


for item in arr:
  m = re.search(r"\(\d{3,4}\)", item)
  
## use if or try/except to catch AttributeError if nothing is found
  if m:
    print(item)
    print(m.group(0)[1:-1])


import re

arr = ["129", "4597", "8989011", "22"]



for item in arr:
  m = re.match(r"^\d{2}(?!\d)", item)
  if m!=None:
    print(m.group())

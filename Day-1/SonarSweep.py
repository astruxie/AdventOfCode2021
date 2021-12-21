# dont know if any of this works yet 

# Variables
count = 0
prev = None

# Iterating through each measurement & comapring
f = open("input.txt", "r")
for measurement in f:
  if measurement > prev:
      # wow, really no ++ operator? wtf snake language
      count = count + 1
  prev = measurement

# print out answer
print("There are " + count + " measurements larger than the previous measurement")
    

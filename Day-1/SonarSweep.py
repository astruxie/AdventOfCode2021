# dont know if any of this works yet 

# Variables
count = 0
prev = 0

# Iterating through each measurement & comapring
f = open("input.txt", "r")
for measurement in f:
  if int(measurement) > int(prev):
      # wow, really no ++ operator? wtf snake language
      count = count + 1
  prev = measurement

#adjust -1 because the first compare is always causing 1 increment, but shouldnt
count = count - 1
# print out answer
print("There are " + str(count) + " measurements larger than the previous measurement")
    

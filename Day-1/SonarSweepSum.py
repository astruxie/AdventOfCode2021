# read in file
# read three at a time and add them
# keep track of previous sum
# compare sum

# Variables
values = []
count = 0
sum = 0
prevSum = 0

# Putting it all into a list for easier indexing
f = open("input.txt", "r")
for measurement in f:
    print(measurement)
    values.append(measurement)


# Doing the adding and comparing
for i, measure in enumerate(values):
    sum = measure + values[i + 1] + values[i + 2]
    print(sum)
    if int(sum) > int(prevSum):
        count+= 1
    prevSum = sum

    
# Adjust my extra compare
count-= 1

# Print out answer
print("There are " + str(count) + " sums greater than the last")
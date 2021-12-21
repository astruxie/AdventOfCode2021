# read in file
# read three at a time and add them
# keep track of previous sum
# compare sum

# Variables
values = []
count = int(0)
summ = 0
prevSum = int(0)

# Putting it all into a list for easier indexing
f = open("input.txt", "r")
for measurement in f:
    values.append(int(measurement))


# Doing the adding and comparing
for i in range(2, len(values)):
    summ = sum(values[i - 2 : i + 1])

    if summ > prevSum:
        count+= 1

    prevSum = summ

    
# Adjust my extra compare
count-= 1

# Print out answer
print(f"There are {count} sums greater than the last")
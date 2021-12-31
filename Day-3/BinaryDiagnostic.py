# read file into list 
# count 1s for each bit and build gamma rate
# find epsilon rate
# convert both to decimal and multiply

# variables
from os import device_encoding


report = []
gammaRatio = [0,0,0,0,0,0,0,0,0,0,0,0]

#each element in list is bit
gamma = []
epsilon = []

# decimal versions 
decG = 0
decE = 0

power = 0

#####################################################################################

# open file and initialize list
f = open("input.txt", "r").read().splitlines()
for byte in f:
    report.append(byte)

# for each ine of this stupid text file
for line in report:
    # for each bit of the line
    for i, bit in enumerate(line):
        # calc num bits in this digit that is a 1
        num = int(bit)
        if num == 1:
            gammaRatio[i]+= 1  


# check those ratios and decide if 1 or 0 for each bit
for num in gammaRatio:
    if (len(report) - num) < num:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

for shit in gamma:
    print(shit)
for shit in epsilon:
    print(shit)


# reverse to make sense with index & power

# convert gamma binary lmao
for i, bit in enumerate(gamma):
    decG += bit * (2**i)

# convert epsilon to binary lmao
for i, bit in enumerate(epsilon):
    decE += bit * (2**i)

power = decG * decE

print (f"The total power consumption is: {power}. yaaaay !")

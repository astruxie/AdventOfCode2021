# variables
pos = 0
depth = 0
value = 0
finalAnswer = 0

# functions
def forward(value, pos):
    pos+= value
    return pos

def down(value, depth):
    depth+= value
    return depth

def up(value, depth):
    depth-= value
    return depth

# open file
f = open("input.txt", "r").read().splitlines()
for instruction in f:
    value = int(instruction[-1])

    if "forward" in instruction:
        pos = forward(value, pos)
    elif "down" in instruction:
        depth = down(value, depth)
    elif "up" in instruction:
        depth = up(value, depth)

finalAnswer = depth * pos

print(f"The answer is {finalAnswer} !!" )
        

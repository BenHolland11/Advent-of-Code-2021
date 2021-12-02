file = open('input.txt', 'r')
lines = file.readlines()
#data = open("day2.in").read().strip().split("\n")


def travel(input):
    depth = 0
    horizontalDistance = 0
    aim = 0
    for line in input:
        if line.split()[0] == 'forward':
            horizontalDistance += int(line.split()[1])
            depth += aim*int(line.split()[1]) 
        elif line.split()[0] == 'up':
            aim -= int(line.split()[1])
        elif line.split()[0] == 'down':
            aim += int(line.split()[1])
    return horizontalDistance*depth

print(travel(lines))
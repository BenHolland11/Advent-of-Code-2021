file = open('input.txt', 'r')
lines = file.readlines()
count = 0

for i in range(len(lines)-1):
    if int(lines[i]) < int(lines[i+1]):
        count+=1
print(count)



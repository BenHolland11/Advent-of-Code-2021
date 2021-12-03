data = open("input.txt").read().strip().split("\n")

result = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in data:
    for i in range(len(line)):
        if int(line[i]) == 0:
            result[i] -= 1
        else:
            result[i] += 1

epsilonRate = []
for i in range(len(result)):
    if result[i] < 1:
        result[i] = 0
        epsilonRate.append(1)
    else:
        result[i] = 1
        epsilonRate.append(0)

z = ''.join(str(e) for e in result)

x = ''.join(str(e) for e in epsilonRate)

print(int(z, 2)*int(x, 2))

        
data = open("input1.txt").read().strip().split("\n")

#find most common bit
#remove all entries that dont contain that bit
#repeat


result = [0,0,0,0,0]
#result = 0
while len(data) > 1:
    for line in data:
        for i in range(len(line)):
            if int(line[i]) == 0:
                result[i] -= 1
            else:
                result[i] += 1
                
    for line in data:
        #print(line)
        for i in range(len(result)-1):
            #print(line[i], result[i])
            if int(result[i]) != int(line[i]):
                try:
                    data.remove(line)
                except ValueError:
                    continue
    result = [0,0,0,0,0]
    print(data)




#z = ''.join(str(e) for e in result)

#x = ''.join(str(e) for e in epsilonRate)



#print(int(z, 2)*int(x, 2))

        
data = open("input.txt").read().strip().split("\n")

def mostCommon(index, data):
    result = 0
    for byte in data:
        if int(byte[index]) == 0:
            result -= 1
        else:
            result += 1
    return correctNumber(result)

def mostCommon2(index, data):
    result = 0
    for byte in data:
        if int(byte[index]) == 0:
            result += 1
        else:
            result -= 1
    return correctNumber2(result)

def correctNumber(bit):
    result = 0
    if bit >= 0:
        result = 1
    else:
        result = 0
    return result

def correctNumber2(bit):
    result = 0
    if bit > 0:
        result = 1
    else:
        result = 0
    return result

def remove(mostCommon, index, oldList):
    newList = []
    if len(oldList) == 1:
        return
    for i in range(len(oldList)):

        if int(oldList[i][index]) == int(mostCommon):
            newList.append(oldList[i])

    return newList



a = remove(mostCommon(0, data),0, data)
b = remove(mostCommon(1, a),1, a)
c = remove(mostCommon(2, b),2, b)
d = remove(mostCommon(2, c),2, c)
e = remove(mostCommon(3, d),3, d)
f = remove(mostCommon(4, e),4, e)
g = remove(mostCommon(5, f),5, f)
h = remove(mostCommon(6, g),6, g)
i = remove(mostCommon(7, h),7, h)
j = remove(mostCommon(8, i),8, i)
k = remove(mostCommon(9, j),9, j)
l = remove(mostCommon(10, k),10, k)
m = remove(mostCommon(11, l),11, l)
print(m)
z = ''.join(str(e) for e in m)

a = remove(mostCommon2(0, data),0, data)
b = remove(mostCommon2(1, a),1, a)
c = remove(mostCommon2(2, b),2, b)
d = remove(mostCommon2(3, c),3, c)
e = remove(mostCommon2(4, d),4, d)
f = remove(mostCommon2(5, e),5, e)
g = remove(mostCommon2(6, f),6, f)
h = remove(mostCommon2(7, g),7, g)
i = remove(mostCommon2(8, h),8, h)
j = remove(mostCommon2(9, i),9, i)
k = remove(mostCommon2(10, j),10, j)
l = remove(mostCommon2(11, k),11, k)


print(l)

x = ''.join(str(e) for e in l)

print(int(z, 2)*int(x, 2))

        

#3573*289


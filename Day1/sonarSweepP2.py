file1 = open('input.txt', 'r')
lines = file1.readlines()

results =[]
i = 0
while i+2 < len(lines):
    sum = int(lines[i].strip()) + int(lines[i+1].strip()) + int(lines[i+2].strip())
    results.append(sum)
    i+=1
    
count = 0
i = 0
while i < len(results)-1:
    if results[i] < results[i+1]:
        count+=1
    i+=1
print(count)

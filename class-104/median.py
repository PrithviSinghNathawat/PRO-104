import csv
with open('data.csv') as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    number=fileData[i][1]
    newData.append(number)
n=len(newData)
newData.sort()
if n%2==0:
    median1=float(newData[n//2])
    median2=float(newData[(n//2)-1])
    median=(median1+median2)/2
else:
    median=float(newData[n//2])
print(median)

#11 python program to read a file and copy only the odd linesw into a new file
#open the first file in read mode
f1=open('file1.txt','r')
#open the second file in write mode
f2=open('file2.txt','w')
file1_cont=f1.readlines()
type(file1_cont)
for i in range(0,len(file1_cont)):
 if(i%2!=0):
  f2.write(file1_cont[i])
else:
    pass
f2=open('file2.txt','r')
file2_cont=f2.read()
print(file2_cont)
f1.close()
f2.close()

import numpy as np
import matplotlib.pyplot as plt

f=open(r"C:\Users\natha\Downloads\tp2019-4.txt","r")
lines=f.readlines()
data=[]
for x in lines:
    data.append(x.split("\t"))
f.close()

time=[]
column_1=[]
column_2=[]
column_3=[]
column_4=[]

for i in range(8002): 
    #print(i)
    time.append(float(data[i%4001][0]))
    column_1.append(float(data[i][1]))
    column_2.append(float(data[i][2]))
    column_3.append(float(data[i][3]))
    column_4.append(float(data[i][4]))
    
plt.figure()
plt.plot(time, column_1)
plt.show()
plt.figure()
plt.plot(time, column_2)
plt.show()
plt.figure()
plt.plot(time, column_3)
plt.show()
plt.figure()
plt.plot(time, column_4)
plt.show()

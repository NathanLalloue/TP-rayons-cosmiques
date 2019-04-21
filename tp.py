#regarde je peux modifier ton fichier
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

for i in range(4000, 8002): 
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

f,ax=plt.subplots(2,2,figsize=(10,3.5))
ax[0,0].plot(time,column_1,'r.',markersize=1.)
ax[0,0].set_title('column_1')
ax[0,0].set_xlabel('temps')
ax[0,0].set_ylabel('Volt')

ax[0,1].plot(time,column_2,'r.',markersize=1.)
ax[0,1].set_title('column_2')
ax[0,1].set_xlabel('temps')
ax[0,1].set_ylabel('Volt')

ax[1,0].plot(time,column_3,'r.',markersize=1.)
ax[1,0].set_title('column_3')
ax[1,0].set_xlabel('temps')
ax[1,0].set_ylabel('Volt')

ax[1,1].plot(time,column_4,'r.',markersize=1.)
ax[1,1].set_title('column_4')
ax[1,1].set_xlabel('temps')
ax[1,1].set_ylabel('Volt')

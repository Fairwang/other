#!user/bin/python
# coding: utf-8
#将adb shell top -d 1 -n 4 | find "baoming  "> D:log.txt
x=[]
y=[]
y1=[]
y2=[]
f0=open('D:\\log.txt','r')
z=len(open('D:\\log.txt','r').readlines())
yta=[]
ytg=[]
print z
while True:
    dat0=f0.readline()
    # for i in range(z):
    if "ta" in dat0:
        x.append(dat0)
        y1.append(x[-1].split('K '))
    if "bg" in dat0:
        y.append(dat0)
        y2.append(y[-1].split('K '))
    if dat0 == '':
        break
print y1
print y2
for j in range(len(y1)):
    yta.append(y1[j][-2])
for j in range(len(y2)):
    ytg.append(y2[j][-2])

#     x.append(dat0.split('K '))
#     if dat0=='':
#         break
# #
# for i in range(z-1):
#     y.append(x[i][-2])
#     if i%2==0:
#         y1.append(x[i][-2])
#     else:
# #         y2.append(x[i][-2])
# print x
# print y
# print y1
# print y2
print yta
print ytg
f0.close()


import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
# a=range(0,(z-1)/2)
fig1=plt.figure("test")
plt.title('neicun',size=14)
plt.xlabel("time",size=14)
plt.ylabel("RSS")
plt.plot(range(len(y1)),yta,color='b',linestyle='--',marker='o',label='yta')#横坐标和描点数保持一致
plt.plot(range(len(y2)),ytg,color="r",linestyle='--',label='ybg')

plt.legend(loc='upper left')
plt.savefig('D:\\plot1.png',format='png')#先保存后展示
plt.show()

#used libraries
from numpy import *


#functions
def cusFact(n):
    if(n<=1):
        return 1
    else:
        return (n* cusFact(n-1))
def Ckn(k,n):
    return cusFact(n)/(cusFact(k)*cusFact(n-k))
def Akn(k,n):
    return cusFact(n)/cusFact(n-k)
def bayeS(bray):
    weighto=0
    sum=0
    for i in range(len(bray)):
        weighto += bray[i][0]
    for i in range(len(bray)):
        bray[i][0]=bray[i][0]/weighto
    for i in range(len(bray)):
        sum+=bray[i][0]*bray[i][1]
    return sum
def bayeI(bray,wI):
    weighto=0
    sum=0
    for i in range(len(bray)):
        weighto += bray[i][0]
    for i in range(len(bray)):
        bray[i][0]=bray[i][0]/weighto
    for i in range(len(bray)):
        sum+=bray[i][0]*bray[i][1]
    return bray[wI][0]*bray[wI][1]/sum
print("=>1.")
print((22+12)/(40+26+22+12))
print("=>2.")
print(Ckn(2-1,10-8)*Ckn(1,8)/Ckn(2,10))
print("=>3.")
print(Ckn(3-1,10-2)*Ckn(1,2)/Ckn(3,10))
print("=>4.")
print(round(1-0.15-0.25-0.2-0.1,5))#це потрібно бо пітон трошки неточний в далеких десятичних і писав би 0.299999999993.це не завжди потрібно бо в основному зайві числа після точки нам не заважають
print("=>5.")
print(Ckn(2,80)/Ckn(2,120))
print("=>6.")
print(round(0.9*0.8,5))
print("=>7.")
Ph=10/20*40/40*39/39*38/38
Pm=7/20*35/40*34/39*33/38
Pl=3/20*10/40*9/39*8/38
Ps=Ph+Pm+Pl
print("Pch="+str(Ph/Ps))
print("Pcl="+str(Pl/Ps))
print("=>8.")
arr8=[[40,0.9],[30,0.95],[30,0.95]]
print(round(bayeS(arr8),5))
print("=>9.")
arr9=[[40,0.8],[30,0.7],[30,0.85]]
print(bayeI(arr9,1))
print("=>10.")
arr10=[[30,0.9],[70,0.8]]
print(1-bayeI(arr10,0))

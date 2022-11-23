#used libraries
from numpy import *
from numpy.linalg import *
from matplotlib.pyplot import *

#start
filename = input() #"input_100.txt"
f = open(filename,"r")#opens file
len = int(f.readline())#takes file length from first line
datarrX = []
datarrY = []
templine=''
for x in range(len):
    templine=f.readline().split()
    datarrX.append(float(templine[1]))
    datarrY.append(float(templine[0].replace(',','.')))
f.close()#closes input file

#measurements to txt
f = open("output from("+filename+").txt","w")
#center of mass
CoM=[0,0]
for i in range(len):
    CoM[0]=CoM[0]+datarrX[i]
    CoM[1]=CoM[1]+datarrY[i]
CoM[0]=CoM[0]/len
CoM[1]=CoM[1]/len
f.write("center of mass="+str(CoM)+'\n')
#covariance
cov=0
cor=0
for i in range(len):
    cov+=(datarrX[i]-CoM[0])*(datarrY[i]-CoM[1])
f.write("covariance="+str(cov/(len-1))+'\n')
devsumX=0.0
devsumY=0.0
for i in range(len):
    devsumX+=(datarrX[i]-CoM[0])**2
    devsumY+=(datarrY[i]-CoM[1])**2
sdevX=sqrt(devsumX/(len-1))
sdevY=sqrt(devsumY/(len-1))
cor=cov/sqrt(devsumX*devsumY)
f.write("correlation="+str(cor)+'\n')
#regression line Y=AX+B
A=cor*sdevX/sdevY
B=CoM[0]-A*CoM[1]
f.write("for a regression formula of type y=a*x+b:\nA="+str(A)+'\n')
f.write("B="+str(B)+'\n')
f.write("y=x*"+str(A)+'+'+str(B)+'\n')

#diagrams
scatter(datarrX,datarrY,datarrX,datarrY)
scatter(CoM[0],CoM[1],color=(0,0,0),s=100,marker='X')#center of mass

x = linspace(10,90,300)
y = x/A
plot(x, y, '-r', label='y=ax+b')

savefig("scatter plot from("+filename+").png",bbox_inches='tight',pad_inches=0)#saves file
clf()#erases the previous plot

f.close()#closes output file
#end
#used libraries
from numpy import *
from numpy.linalg import *
from matplotlib.pyplot import *
from stemgraphic import *
import pandas as pd

#functions
def cusquantile(cqnda,cloc):#custom function for finding quantiles
    lower = int(floor((len)*cloc))-1
    upper = int(ceil((len)*cloc))-1
    return cqnda[lower]+(cqnda[upper]-cqnda[lower])*cloc

#start
filename = input()
f = open(filename,"r")#opens file
len = int(f.readline())#takes file length from first line
datarray = []#initialises data array
for x in range(len):
    datarray.append(int(f.readline()))
f.close()#closes input file
datarray = sort(datarray)

#measurements to txt
f = open("output from("+filename+").txt","w")
f.write("P25="+str(cusquantile(datarray,0.25))+'\n')
f.write("P75="+str(cusquantile(datarray,0.75))+'\n')
f.write("P90="+str(cusquantile(datarray,0.90))+'\n')
f.write("average="+str(average(datarray))+'\n')
devsum = 0.0
for i in range(len):
    devsum = devsum + (float(datarray[i])-(float(datarray.sum())/len))**2#half of the standard deviation formula
f.write("standard deviation = "+str(sqrt(devsum/(len-1)))+'\n')#second half
zscores = [(value - (datarray.sum()/len)) / sqrt(devsum/(len-1)) for value in datarray]
f.write("Z-scores="+str(zscores)+'\n')

#figure out the scale formula for 95
A = array([[100,1],[average(datarray),1]])
B = array([100,95])
a,b = solve(A,B)
f.write("a and b needed to scale grades to 95:\na="+str(a)+'\nb='+str(b))
f.write("\nfunction:\ny="+str(a)+'*x+'+str(b)+'\nresulting data:')
for k in range(len):
    f.write('\n'+str(round(datarray[k]*a+b)))
f.close()

#diagrams
y = pd.Series(datarray)
fig, ax = stem_graphic(y,delimiter_color='C2',median_alpha=0,alpha=0.05,break_on=30)
savefig("leafstem plot from("+filename+").png",bbox_inches='tight',pad_inches=0)#saves file
clf()#erases the previous plot
fig = boxplot(datarray,vert=False)
savefig("boxplot plot from("+filename+").png",bbox_inches='tight',pad_inches=0)#saves file

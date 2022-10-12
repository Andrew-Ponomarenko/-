#used libraries
from numpy import *
from matplotlib.pyplot import *

filename = raw_input()
f = open(filename,"r")#opens file
len = int(f.readline())#takes file length from first line
datarray = []#initialises data array
for x in range(len):
    datarray.append(int(f.readline()))

datarray = sort(datarray)
fig = hist(datarray)#draws histogram
#writes data properties onto the histogram
title('data histogram')
#labels
xlabel('value')
ylabel('frequency')
savefig("output from "+filename+".png")#saves file
#properties but more manual
f.close()
f = open("output from "+filename+".txt","w")
if (len % 2) == 1:#check odd
    f.write("Median = "+str(datarray[len/2]))
else:
    f.write("Median = "+str((datarray[int(len/2)]+datarray[int(len/2+1)])/2))
largestCount = 0
for i in range(len):#custom function for finding mode
        count = count_nonzero(datarray==datarray[i])
        if(count > largestCount):
            largestCount = count
            valuePosition = i
        i += count
f.write("\nmode = "+str(datarray[valuePosition]))
f.write("\ndispersion = "+str(float(datarray.max()-datarray.min())/float(datarray.max()+datarray.min())))
devsum = 0.0#initialises as float
for i in range(len):
    devsum = devsum + (float(datarray[i])-(float(datarray.sum())/len))**2#half of the standard deviation formula
f.write("\nstandard deviation = "+str(sqrt(devsum/(len-1))))#second half
def cusquantile(cqnda,cloc):#custom function for finding quantiles
    return cqnda[int(floor(len*cloc))]+(cqnda[int(ceil(len*cloc))]-cqnda[int(floor(len*cloc))])*((len*cloc) % 1)
f.write("\nquartile deviation = "+str((cusquantile(datarray,0.75)-cusquantile(datarray,0.25))/2))
f.close()

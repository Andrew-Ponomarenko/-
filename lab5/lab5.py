from numpy import *

def cusFact(n):
    if(n<=1):
        return 1
    else:
        return (n* cusFact(n-1))


def binomial(n, p, x, mode):
    chances=zeros(n+1)
    if(x<=n):
        if(n<150):  #при цифровій обробці поріг обчислюємих факторіалів вище ніж в ручну
            for i in range(n+1):
                chances[i]=(cusFact(n))*(p**i)*((1-p)**(n-i))/(cusFact(n-i)*cusFact(i))     #звичайний біноміал
        else:
            for i in range(n+1):
                chances[i]=1.0/sqrt(2*pi*n*p*(1-p)) * exp(-(i-n*p)**2/(2*n*p*(1-p)))    #біноміал через нормальний розподіл
        if(mode == '>x'):
            return sum(chances[(x+1):n+1])      #виводить всі шанси вище x
        if(mode == '<x'):
            return sum(chances[0:x])    #виводить всі шанси низще x
        if(mode == '=x'):
            return chances[x]   #виводить тільки шанс x
        if(mode == 'max'):
            return argmax(chances)   #виводить індекс найвищого шансу і ігнорує x,можна булоб просто помножити n на p але всеодно ця таблиця уже зроблена
        if(mode == 'min'):
            return argmin(chances)   #виводить індекс найменшого шансу і ігнорує x
    else:
        return 0    #якщо x більше ніж кількість спроб то шанс 0
#main

print("1\t"+str(binomial(5,0.2,3,'=x')))
print("2.a\t"+str(binomial(5,0.8,4,'=x')))
print("2.b\t"+str(binomial(5,0.8,4,'=x')+(binomial(5,0.8,4,'>x'))))
print("3\t"+str(binomial(400,0.2,80,'=x')))
print("4\t"+str(binomial(100000,0.0001,5,'=x')))
print("5\t"+str(binomial(600,0.4,228,'>x')-binomial(600,0.4,251,'>x')))
print("6\t"+str(binomial(100,0.4,0,'max'))+"\t,\t"+str(binomial(100,0.4,binomial(100,0.4,0,'max'),'=x')))
print("7\t"+str(binomial(4000,0.04,171,'<x')))
print("8\t"+str(binomial(10000,0.5,5000,'=x')))
print("9\t"+str(binomial(1000,0.002,5,'=x')))
print("10\t"+str(binomial(150,(1-0.03),0,'max')))
#Julius R, v1.8, 25/03-2021
def ptOpTilN(n): #Funktion som finder primtal op til n
    ptOpTilNList = []
    for num in range(2,n+1):
        isPrime = True
        for i in range(2,num):
            if num%i == 0:
                isPrime = False
        if isPrime:
            ptOpTilNList.append(num)
    return ptOpTilNList



def størstePrimFaktor(n): #Funktion som et tal n's største primfaktor
    i = 2
    while i * i <= n:
        if n % i != 0:
            i = i + 1
        else:
            n = n // i
    return n                                  


def stærkPrimtalFinder(a,b): #Funktion som finder primtal mellem a og b
    primtalInInterval = [i for i in range(a,b+1) if i in ptOpTilN(b)]
    stærkePrimtal = []
    for p in primtalInInterval:
        if p < 256:
            continue
        if størstePrimFaktor(p-1) < 100:
            continue
        if størstePrimFaktor(p+1) < 100:
            continue
        if størstePrimFaktor(størstePrimFaktor(p-1)-1) < 100:
            continue
        stærkePrimtal.append(p)
    return stærkePrimtal

lower = int(input("Nedre grænse?"))
upper = int(input("Øvre grænse?"))

print(stærkPrimtalFinder(lower,upper))
        

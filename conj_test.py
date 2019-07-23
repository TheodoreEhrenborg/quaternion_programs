def c1(n):#Given an odd prime n, n=twin prime+2*triangle number
    from mymath import isprime
    if n==2:
        return True
    if not(isprime(n)):
        return True
    k=0
    while True:
        p=n-k*(k+1)#p could be the twin prime
        if p<3:
            return False
        i=isprime(p)
        if i and isprime(p-2):
            return True
        if i and isprime(p+2):
            return True
        k=k+1
def test(f,start,end,checkup=None,soft=False):
    if f=="c1":
        g=c1
    if f=="c3":
        g=c3   
    if f=="c4":
        g=c4   
    if f=="c5":
        g=c5  
    if f=="c6":
        g=c6   
    if f=="c7":
        g=c7   
    if f=="c8":
        g=c8   
    good=True
    for x in range(start,end+1):
        result=g(x)
        if not(result):
            if soft:
                print "Failed at "+str(x)
                good=False
            else:
                return "Failed at"+str(x)
        if checkup!=None:
            if x%checkup==0:
                print "Checked through",x
    if good:
        return 'Success'
    else:
        return 'Failure'
def c2(n):#Given an odd prime n, n=twin prime+2*triangle number,returns all representations 
    from mymath import isprime
    if n==2:
        return []
    if not(isprime(n)):
        return []
    k=0
    repr_list=[]
    while True:
        p=n-k*(k+1)#p could be the twin prime
        if p<3:
            return repr_list
        i=isprime(p)
        if i and isprime(p-2):
            repr_list.append([k*(k+1),p])
        if i and isprime(p+2):
            repr_list.append([k*(k+1),p])
        k=k+1
def c3(n):#Given an odd prime n, n=twin prime+square number
    from mymath import isprime
    if n==2:
        return True
    if not(isprime(n)):
        return True
    k=0
    while True:
        p=n-k**2#p could be the twin prime
        if p<3:
            return False
        i=isprime(p)
        if i and isprime(p-2):
            return True
        if i and isprime(p+2):
            return True
        k=k+1
def c4(n):#Given an odd prime n, n=twin prime+2*square number
    from mymath import isprime
    if n==2:
        return True
    if not(isprime(n)):
        return True
    k=0
    while True:
        p=n-2*k**2#p could be the twin prime
        if p<3:
            return False
        i=isprime(p)
        if i and isprime(p-2):
            return True
        if i and isprime(p+2):
            return True
        k=k+1
def c5(n):#Given an odd prime n, n=prime+2*square number
    from mymath import isprime
    if n==2:
        return True
    if not(isprime(n)):
        return True
    k=1#If k is 0, p=n, so p is prime
    while True:
        p=n-2*k**2#p could be the prime
        if p<3:
            return False
        i=isprime(p)
        if i:
            return True
        k=k+1
def c6(n):#Given an odd prime n, n=prime+square number
    from mymath import isprime
    if n==2:
        return True
    if not(isprime(n)):
        return True
    k=1#If k is 0, p=n, so p is prime
    while True:
        p=n-k**2#p could be the prime
        if p<2:
            return False
        i=isprime(p)
        if i:
            return True
        k=k+1
def c7(n):#Given an odd prime n, n=prime+k*(k+3)
    from mymath import isprime
    if n==2:
        return True
    if not(isprime(n)):
        return True
    k=1#If k is 0, p=n, so p is prime
    while True:
        p=n-k*(k+3)#p could be the prime
        if p<2:
            return False
        i=isprime(p)
        if i:
            return True
        k=k+1
def c8(n):#Given an odd prime n, n=twin prime+k*(k+3)
    from mymath import isprime
    if n==2:
        return True
    if not(isprime(n)):
        return True
    k=0
    while True:
        p=n-k*(k+3)#p could be the twin prime
        if p<3:
            return False
        i=isprime(p)
        if i and isprime(p-2):
            return True
        if i and isprime(p+2):
            return True
        k=k+1

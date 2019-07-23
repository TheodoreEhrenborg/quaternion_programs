def main(end):
    import math
    import mymath
    l=[]
    ##print mymath.gcf(2,5)
    ##print(help(math))
    for a in range(0,end+1):
        for b in range(a,end+1):
            for c in range(b,end+1):
                for d in range(c,end+1):
                    e=math.sqrt(a*a+b*b+c*c+d*d)
                    if int(e)==e and mymath.gcf(mymath.gcf(mymath.gcf(a,b),c),d)==1:
    ##                    print a,b,c,int(d)
                        l.append([float(a),float(b),float(c),float(d),float(e)])
    return l
def main2(end):
    import math
    import mymath
    end=float(end)
    l=[]
    ##print mymath.gcf(2,5)
    ##print(help(math))
    for a in half_range(0,end+.5):
        for b in half_range(a,end+.5):
            for c in half_range(b,end+.5):
                for d in half_range(c,end+.5):
                    e=float(math.sqrt(a*a+b*b+c*c+d*d))
                    if int(e)!=e and int(e+.5)!=e+.5:#Modulus is irrational
                        continue
                    if (int(a)==a and int(b)==b and int(c)==c and int(d)==d) and mymath.gcf(mymath.gcf(mymath.gcf(a,b),c),d)==1 and not(a%2 and b%2 and c%2 and d%2):
                        l.append([float(a),float(b),float(c),float(d),float(e)])
                    if int(a+.5)==a+.5 and int(b+.5)==b+.5 and int(c+.5)==c+.5 and int(d+.5)==d+.5 and mymath.gcf(mymath.gcf(mymath.gcf(a,b),c),d)==.5:
                        l.append([float(a),float(b),float(c),float(d),float(e)])
##and (int(a+.5)!=a+.5 or int(b+.5)!=b+.5 or int(c+.5)!=c+.5 or int(d+.5)!=d+.5):
    return l
def half_range(start,end):
    l=range(int(2*start),int(2*end))
    n=[]
    for x in l:
        n.append(float(x)/2)
    return n
##print main(10)


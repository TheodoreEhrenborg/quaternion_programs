import findingquintuples, quaternion
q_list=findingquintuples.main(20)
units=[quaternion.Quaternion(0.5,-0.5,-0.5,-0.5), quaternion.Quaternion(-1.0,0.0,0.0,0.0), quaternion.Quaternion(-0.5,-0.5,-0.5,-0.5), quaternion.Quaternion(-0.5,-0.5,-0.5,0.5), quaternion.Quaternion(-0.5,-0.5,0.5,-0.5), quaternion.Quaternion(-0.5,-0.5,0.5,0.5), quaternion.Quaternion(-0.5,0.5,-0.5,-0.5), quaternion.Quaternion(-0.5,0.5,-0.5,0.5), quaternion.Quaternion(-0.5,0.5,0.5,-0.5), quaternion.Quaternion(-0.5,0.5,0.5,0.5), quaternion.Quaternion(0.0,-1.0,0.0,0.0), quaternion.Quaternion(0.0,0.0,-1.0,0.0), quaternion.Quaternion(0.0,0.0,0.0,-1.0), quaternion.Quaternion(0.0,0.0,0.0,1.0), quaternion.Quaternion(0.0,0.0,1.0,0.0), quaternion.Quaternion(0.0,1.0,0.0,0.0), quaternion.Quaternion(0.5,-0.5,0.5,-0.5), quaternion.Quaternion(0.5,-0.5,0.5,0.5), quaternion.Quaternion(0.5,0.5,-0.5,-0.5), quaternion.Quaternion(0.5,0.5,-0.5,0.5), quaternion.Quaternion(0.5,0.5,0.5,-0.5), quaternion.Quaternion(0.5,-0.5,-0.5,0.5), quaternion.Quaternion(0.5,0.5,0.5,0.5), quaternion.Quaternion(1.0,0.0,0.0,0.0)]
#Conjecture: Perhaps the numbers of the quintuple matter more for factorablity than the signs or order
def L1():#Shows that not every quintuple can be factored using Quadrant 1 using Lipschitz#POSSIBLE ERROR
    for x in q_list: print len(quaternion.pyth_factor2(quaternion.Quaternion(0,0,0,0,use_list=True,l=x),True)),x
def H1():#Shows that every quintuple can be factored using Quadrant 1 using Hurwitz#POSSIBLE ERROR 
    for x in q_list: print len(quaternion.pyth_factor(quaternion.Quaternion(0,0,0,0,use_list=True,l=x),True,False)),quaternion.Quaternion(0,0,0,0,use_list=True,l=x)
def L2():#Shows the quintuples that are squares using Lipschitz#POSSIBLE ERROR 
    for x in q_list:
        works=False
        factored_list=quaternion.pyth_factor2(quaternion.Quaternion(0,0,0,0,use_list=True,l=x))
        for y in factored_list:
            if y[0]==y[1]:
                works=True
        if works:
            print 
def H2():#Shows the quintuples that are squares using Hurwitz#POSSIBLE ERROR 
    for x in q_list:
        works=False
        factored_list=quaternion.pyth_factor(quaternion.Quaternion(0,0,0,0,use_list=True,l=x))
        for y in factored_list:
            if y[0]==y[1]:
                works=True
        if works:
            print x
def X1(bound=10):#Tries to find any square quintuples in Quadrant 1
    q=set()
    for aa in range(-bound,bound):
        for bb in range(-bound,bound):
            for cc in range(-bound,bound):
                for dd in range(-bound,bound):
                    A=float(aa)/2
                    B=float(bb)/2
                    C=float(cc)/2
                    D=float(dd)/2
                    r=quaternion.Quaternion(A,B,C,D)
                    s=r*r
                    if s.quadrant1 and s.Hurwitz and not(s.reducible):
##                        print s
                        q.add((s.a,s.b,s.c,s.d))
    return q
def L3():#Prints the Lipschitz factorizations of integer quintuples in Quadrant 1
    the_list=[]#It appears that 1+2i+8j+10k and 2+4i+7j+10k cannot be factored, even using Hurwitz quaternions.
    for x in q_list:
        the_list.append([quaternion.pyth_factor2(quaternion.Quaternion(0,0,0,0,use_list=True,l=x),False,False),quaternion.Quaternion(0,0,0,0,use_list=True,l=x)])
##        print 2
##    print 3
    for y in the_list:
        print "----------"
        for z in y[0]:#y[0] is the list of factors, y[1] is the quintuple written as a quaternion
            print str(y[1])+'=('+str(z[0])+')*('+str(z[1])+')'
def H3():#Prints the Hurwitz factorizations of integer quintuples in Quadrant 1
    the_list=[]#It appears that 1+2i+8j+10k and 2+4i+7j+10k cannot be factored, even using Hurwitz quaternions.
    for x in q_list:
        the_list.append([quaternion.pyth_factor(quaternion.Quaternion(0,0,0,0,use_list=True,l=x),False,False),quaternion.Quaternion(0,0,0,0,use_list=True,l=x)])
##        print 2
##    print 3
    for y in the_list:
        print "----------"
        for z in y[0]:#y[0] is the list of factors, y[1] is the quintuple written as a quaternion
            print str(y[1])+'=('+str(z[0])+')*('+str(z[1])+')'
#Every quintuple can be factored into two quaternions, each with the square root of the magnitude of the quintuple. However, it may be impossible for some quintuples to force its factors to use the same numbers.
def H4():#Tries to find some Hurwitz factors of the quintuple 1,2,8,10 using the same number
    print [quaternion.pyth_factor(quaternion.Quaternion(1,2,8,10),False,True),quaternion.Quaternion(1,2,8,10)]
    print [quaternion.pyth_factor(quaternion.Quaternion(-1,2,8,10),False,True),quaternion.Quaternion(-1,2,8,10)]
    print [quaternion.pyth_factor(quaternion.Quaternion(1,-2,8,10),False,True),quaternion.Quaternion(1,-2,8,10)]
    print [quaternion.pyth_factor(quaternion.Quaternion(1,2,-8,10),False,True),quaternion.Quaternion(1,2,-8,10)]
    print [quaternion.pyth_factor(quaternion.Quaternion(1,2,8,-10),False,True),quaternion.Quaternion(1,2,8,-10)]
    print [quaternion.pyth_factor(quaternion.Quaternion(-1,-2,8,10),False,True),quaternion.Quaternion(-1,-2,8,10)]
    print [quaternion.pyth_factor(quaternion.Quaternion(1,-2,-8,10),False,True),quaternion.Quaternion(1,-2,-8,10)]
    print [quaternion.pyth_factor(quaternion.Quaternion(1,-2,8,-10),False,True),quaternion.Quaternion(1,-2,8,-10)]
    import os
    os.system("say 'Done'")
def H5():#Tries to find some Hurwitz factors of 1,2,8,10 by multiplying it by the units
    for x in units:
        print quaternion.pyth_factor(quaternion.Quaternion(1,2,8,10)*x),quaternion.Quaternion(1,2,8,10)*x
    import os
    os.system("say 'Done'")
def H6():#Be thorough. Permutes 1,2,8,10 and multiplies by the units. H6 failed
    print 8*24
    for x in units:
        print quaternion.pyth_factor(quaternion.Quaternion(1,2,8,10)*x,False,True),quaternion.Quaternion(1,2,8,10)*x
        print quaternion.pyth_factor(quaternion.Quaternion(-1,2,8,10)*x,False,True),quaternion.Quaternion(-1,2,8,10)*x
        print quaternion.pyth_factor(quaternion.Quaternion(1,-2,8,10)*x,False,True),quaternion.Quaternion(1,-2,8,10)*x
        print quaternion.pyth_factor(quaternion.Quaternion(1,2,-8,10)*x,False,True),quaternion.Quaternion(1,2,-8,10)*x
        print quaternion.pyth_factor(quaternion.Quaternion(1,2,8,-10)*x,False,True),quaternion.Quaternion(1,2,8,-10)*x
        print quaternion.pyth_factor(quaternion.Quaternion(-1,-2,8,10)*x,False,True),quaternion.Quaternion(-1,-2,8,10)*x
        print quaternion.pyth_factor(quaternion.Quaternion(1,-2,-8,10)*x,False,True),quaternion.Quaternion(1,-2,-8,10)*x
        print quaternion.pyth_factor(quaternion.Quaternion(1,-2,8,-10)*x,False,True),quaternion.Quaternion(1,-2,8,-10)*x
    import os
    os.system("say 'Done'")
def X2():#Finds the units
    u=[]
    for a in range(-2,3):
        for b in range(-2,3):
            for c in range(-2,3):
                for d in range(-2,3):
                    A=float(a)/2
                    B=float(b)/2
                    C=float(c)/2
                    D=float(d)/2
                    q=quaternion.Quaternion(A,B,C,D)
                    if q.modulus==1:
                        u.append(q)
    print u
def X3(value):#PROBLEM: quaternions cannot handle becoming sets
    import math
    list=findingquintuples.main(value)
    new=[]
##    print 53
    for x in list:
        if x[0]%2 and x[2]%2 and x[2]%2 and x[3]%2:
            new.append([float(x[0])/2,float(x[1])/2,float(x[2])/2,float(x[3])/2])
        else:
            new.append([float(x[0]),float(x[1]),float(x[2]),float(x[3])])
##    print 54
    return new
##    squared=X1(value)
##    print 55
##    for x in new:
##        print 56
##        if x in squared:
##            print 1,x
##        elif x*2 in squared:
##            print 2,x
##        else:
##            print 0,x
def X4(v):#Prints quintuples nicely
    l=findingquintuples.main2(v)
    for quintuple in l:
        p=''
        for y in quintuple:
            Y=str(y)
            if Y[-2:]=='.0':
                p+=Y[:-2]
                k=len(Y)-2
            else:
                p+=Y
                k=len(Y)
            for z in range(0,5-k):
                p+=' '
        print p
def X5_help():#Makes permutation list
    p=[]
    for x in range(0,24):
        q=[0,0,0,0]
        q[0]=input()
        q[1]=input()
        q[2]=input()
        q[3]=input()
        p.append(q)
    print p
def X5():#Tries every option to deal with 1,2,8,10,13
    goal = [1,2,8,10]
    import os
    options = [ [0,0,2,3] , [1,2,2,2] ,[3.5, .5, .5, .5] , [2.5, 2.5 , .5, .5], [2.5, 1.5 , 1.5, 1.5] ]
    units1 = [quaternion.i() , quaternion.j() , quaternion.k() , 1]
    units2 = [quaternion.Quaternion(0.5,0.5,0.5,0.5), quaternion.Quaternion(1.0,0.0,0.0,0.0), quaternion.Quaternion(0.5,0.5,0.5,-0.5), quaternion.Quaternion(0.5,0.5,-0.5,0.5), quaternion.Quaternion(0.5,-0.5,0.5,0.5), quaternion.Quaternion(0.5,0.5,-0.5,-0.5), quaternion.Quaternion(0.5,-0.5,-0.5,0.5), quaternion.Quaternion(0.5,-0.5,0.5,-0.5), quaternion.Quaternion(0.5,-0.5,-0.5,-0.5)]
    signs = [-1,1]
##    perms=[[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1], [1, 2, 3, 0], [1, 2, 0, 3], [1, 3, 0, 2], [1, 3, 2, 0], [1, 0, 2, 3], [1, 0, 3, 2], [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 3, 0], [2, 1, 0, 3], [2, 3, 1, 0], [2, 3, 0, 1], [3, 2, 1, 0], [3, 2, 0, 1], [3, 1, 0, 2], [3, 1, 2, 0], [3, 0, 2, 1], [3, 0, 1, 2]]
    perms = [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1], [1, 0, 2, 3], [1, 0, 3, 2], [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0], [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 0, 3], [2, 1, 3, 0], [2, 3, 0, 1], [2, 3, 1, 0], [3, 0, 1, 2], [3, 0, 2, 1], [3, 1, 0, 2], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0]]
    for factor in options:
        if factor[0]**2 + factor[1]**2 + factor[2]**2 + factor[3]**2 != 13:
            print "error1", factor
            break
        for s0 in signs:
            for s1 in signs:
                for s2 in signs:
                    for s3 in signs:
                        print "Status:",factor,s0,s1,s2,s3
                        for p in perms:
                            f1 = s0*factor[0]*units1[p[0]] + s1*factor[1]*units1[p[1]] + s2*factor[2]*units1[p[2]] + s3*factor[3]*units1[p[3]]
                            
                            for S0 in signs:
                                for S1 in signs:
                                    for S2 in signs:
                                        for P in perms:
                                            f2 = S0*factor[0]*units1[P[0]] + S1*factor[1]*units1[P[1]] + S2*factor[2]*units1[P[2]] + factor[3]*units1[P[3]]
                                            for U in units2:
                                                product = f1 * f2 * U
                                                product_list = product.coeffient_list
                                                new=[]
                                                for x in product_list:
                                                    new.append(abs(round(x,1)))
                                                new.sort()
##                                                print "hi"
                                                if new == goal:
                                                    print "Success!", f1, f2, U, product
                                                    os.system("say 'Success''")
    print "Failure! Time to revise hypothesis!"
    os.system("say 'Failure! Time to revise hypothesis!'")
                                                

'''Classes to use for the data-gathering program for the quaternions project'''
from quaternion import Quaternion
class GenList:
    '''A list that holds the generating numbers (usually all>=0)
    and also remembers which formulas/quadruples worked with it'''
    def __init__(self,input_list):
        self.num_list = input_list
        self.friends=[]
    def copy(self):
        '''returns a copy with no friends'''
        return GenList(self.num_list)
    def makeFriends(self,q,f):
        '''adds a copy of a quadruple and a formula to its list'''
        self.friends.append( [q.copy(),f.copy()] )
    def toQuaternion(self):
        return Quaternion( use_list = True, l = self.num_list[:] )
    def __str__(self):
        output=""
        for x in self.num_list:
            output+=str(x)+" "
        return output
    @classmethod
    def findAll(cls,limit):
        '''Returns all integer and half-interver GenLists, in one list, that 
        could produce a Pythagorean quintuplw that fits in the Quadrant 1
        hypercube with side length of limit'''
        #A genList is either all half-integer or all integers
        the_list = []
        import math
        bound = int( math.sqrt( 2 * float(limit) ) ) + 1
        for a in range(0,bound):
            for b in range(0,bound):
                for c in range(0,bound):
                    for d in range(0,bound):
                        if a**2 + b**2 + c**2 + d**2 <= 2*limit:
                            the_list.append(GenList([a,b,c,d]))
                        halfA = float(a)+.5
                        halfB = float(b)+.5
                        halfC = float(c)+.5
                        halfD = float(d)+.5
                        if halfA**2 + halfB**2 + halfC**2 + halfD**2 <= 2*limit:
                            the_list.append( GenList( [ halfA, halfB, halfC, halfD] ) )
        return the_list
class Formula:
    '''A transformation that, given a genList, turns it into two quaternions
    (applying the necessary Permuation and Signer)  
    and calculates their product as a quaternion.
    Returns the product as a Quadruple, which can be compared to a list of given
    Quadruples.
    A Formula also remembers which genLists/quadruples worked with it
    NOT DONE'''
    def __init__( self, perm, sig, serial=0 ):
        self.perm = perm.copy()
        self.sig = sig.copy()
        self.friends=[]
        self.serial = serial
    def __str__(self):
        options = "xyzw"
        output = "(x"
        if self.sig.pList[0]>0:
            output+="+"
        else:
            output+="-"
        output += "yi"
        if self.sig.pList[1]>0:
            output+="+"
        else:
            output+="-"
        output += "zj"
        if self.sig.pList[2]>0:
            output+="+"
        else:
            output+="-"       
        output += "wk)("
        if self.sig.pList[3]>0:
            output+=""
        else:
            output+="-"
        output += options[(self.perm.pList[0]-1)]
        if self.sig.pList[5]>0:
            output+="+"
        else:
            output+="-"
        output += options[(self.perm.pList[1]-1)]
        output += "i"
        if self.sig.pList[5]>0:
            output+="+"
        else:
            output+="-"
        output += options[(self.perm.pList[2]-1)]
        output += "j"
        if self.sig.pList[6]>0:
            output+="+"
        else:
            output+="-" 
        output += options[(self.perm.pList[3]-1)]
        output += "k)"
        return output
    def copy(self):
        '''returns a copy with no friends'''
        return Formula(self.perm, self.sig,self.serial)
    def makeFriends(self,q,g):
        '''adds a copy of a quadruple and a genList to its list'''
        self.friends.append( [q.copy(),g.copy()] )
    def actUpon(self,g):
        '''Applies a permutation and a signer to make an altered
        version of g, multiples g by g prime, and returns the 
        result as a Quadruple.'''
        g=g.copy()#Just to be safe
        g_prime = self.perm.permute(g)
        l=self.sig.sign(g,g_prime)
        g=l[0]
        g_prime=l[1]
        q = g.toQuaternion() * g_prime.toQuaternion()
        return Quadruple(q)
    @classmethod
    def everyFormula(cls):
        '''Finds all 24*128 formulas and returns the unique ones in a list'''
        import math
        l = []
        for s in Signer.allSigners():
            for p in Permutation.allPermutations():
                l.append( Formula(p,s) )
        #l has 3072 elements -- too many
        g = GenList( [ math.pi, math.e , math.sqrt(2), math.sqrt(5) ] )
        results = []
        differentFormulas = []
        for f in l:
            q = f.actUpon(g)
            if q not in results:
                results.append(q)
                differentFormulas.append(f)
        k=1
        for x in differentFormulas:
            x.serial=k
            k+=1
        return differentFormulas
class Permutation:
    '''A transformation that, given a genList, permutes it into a different order.
    Does not permute in-place''' 
    def __init__(self, seedList):
        '''A seedList could look like [1,3,4,2]'''
        self.pList = seedList[:]
    def copy(self):
        '''returns a copy'''
        return Permutation(self.pList)
    def __str__(self):
        return str(self.pList)
    def permute(self, g):
        '''returns a permuted version of a GenList'''
        return GenList( [ g.num_list[ self.pList[0] - 1 ] , g.num_list[ self.pList[1] - 1 ] , g.num_list[ self.pList[2] - 1 ] , g.num_list[ self.pList[3] - 1 ] ] )
    @classmethod
    def allPermutations(cls, index=4 ):
        '''Returns all permutations in a list for a certain index.
        For instance, index = 3 --> 012 021 120 102 210 201 
        Right now, it only works for index=4'''
        if index == 4:
            bigL = []
            l = [1,2,3,4]
            for a in l:
                l2=l[:]
                l2.remove(a)
                for b in l2:
                    l3 = l2[:]
                    l3.remove(b)
                    for c in l3:
                        l4=l3[:]
                        l4.remove(c)
                        bigL.append([a,b,c,l4[0] ] )
            list2 = []
            for x in bigL:
                list2.append( Permutation( x ) )
            return list2
class Quadruple:
    '''Given a quaternion (usually 80% of a Pythagorean quintuple), a quadruple strips away signs and order,
    as well as rounding to the nearest 1000th, enabling easy comparison.
    It also remembers which genlists and formulas worked with it.'''
    def __init__(self, input_q):
        self.q = input_q+0#Copies the quaternion
        l = [self.q.a,self.q.b,self.q.c,self.q.d]
        import math
        self.list = []
        for x in l:
            self.list.append( float(int( 1000*math.fabs(float(x))+.5 ))/1000 )
        self.list.sort()
        self.friends = []
    def __eq__(self,other):
        if self.list == other.list:
            return True
        return False
    def copy(self):
        '''Returns a copy with no friends'''
        return Quadruple(self.q)
    def makeFriends(self, f, g):
        '''Adds a copy of a Fromula and a GenList to its list of friends'''
        self.friends.append( [ f.copy(), g.copy() ] )
    def __str__(self):
        output=""
        for x in self.list:
            output+=str(x)+" "
        return output        
    @classmethod
    def convert(cls, listOfLists):
        y = []
        for x in listOfLists:
            q = Quaternion( use_list= True, l=x)
            y.append( Quadruple(q) )
        return y
    @classmethod
    def findHurwitzPythagoreans(cls,cubeEdge):
        import math
        import mymath
        l=[]
        for a in range(0,cubeEdge+1):
            for b in range(a,cubeEdge+1):
                for c in range(b,cubeEdge+1):
                    for d in range(c, cubeEdge+1):
                        e=math.sqrt(a*a+b*b+c*c+d*d)
                        if int(e)==e:
                            if mymath.gcf(mymath.gcf(mymath.gcf(a,b),c),d)==1:
                                l.append([float(a),float(b),float(c),float(d)])
        newL = []
        for i in l:
            if not Quadruple.isAllOdd(i):
                newL.append(i)
        for a in range(0,cubeEdge):
            for b in range(a, cubeEdge):
                for c in range(b,cubeEdge):
                    for d in range(c, cubeEdge):
                        halfA = float(a) + .5
                        halfB = float(b) + .5
                        halfC = float(c) + .5
                        halfD = float(d) + .5
                        e = math.sqrt( halfA**2 + halfB**2 + halfC**2 + halfD**2 )
                        if int(e)==e:
                            if mymath.gcf(mymath.gcf(mymath.gcf(halfA,halfB),halfC),halfD)==0.5:
                                newL.append( [halfA, halfB, halfC, halfD] )
        return newL
    @classmethod
    def isAllOdd(cls, toCheck):
        '''Given a list of 4 elements, returns true if all elements are odd integers'''
        allOdd = True
        for x in toCheck:
            if not( x==int(x) and float(x)/2 != int( float(x)/2 ) ):
                allOdd = False
        return allOdd

class Signer:
    '''A transformation that, given 2 GenLists, changes the sign (or not) of all but the first number in the first''' 
    def __init__(self, seedList):
        '''A seedList could look like [-1,1,1,-1,1,-1,-1].
        It must have 7 elements'''
        self.pList = seedList[:]
    def __str__(self):
        return str(self.pList)
    def copy(self):
        '''returns a copy'''
        return Signer(self.pList)
    def sign(self,g1,g2):
        '''returns a signed version of 2 GenLists (they are in a list of length
        2)'''
        return  [GenList([ g1.num_list[0] , self.pList[0] * g1.num_list[1] , self.pList[1] * g1.num_list[2] , self.pList[2] * g1.num_list[3] ] ) , GenList([ self.pList[3] * g2.num_list[0] , self.pList[4] * g2.num_list[1] , self.pList[5] * g2.num_list[2] , self.pList[6] * g2.num_list[3] ]  ) ]
    @classmethod
    def allSigners(cls):
        '''Returns all 128 Signers.'''
        bigL = []
        for x1 in [-1,1]:
            for x2 in [-1,1]:
                for x3 in [-1,1]:
                    for x4 in [-1,1]:
                        for x5 in [-1,1]:
                            for x6 in [-1,1]:
                                for x7 in [-1,1]:
                                    bigL.append( [x1,x2,x3,x4,x5,x6,x7] )
        list2 = []
        for x in bigL:
            list2.append( Signer( x ) )
        list2.reverse()#Prioritizes Signers that don't change many signs 
        return list2
class Manager():
    '''Handles pickling of data.
    Thanks to 
    https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory'''
    def __init__(self):
        import os
        os.system(" rm SF18_Helper.txt")
        folder_exists = False
        os.system(" ls  >> SF18_Helper.txt")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        f=open(dir_path + "/SF18_Helper.txt","r")
        for line in f:
            if "Quaternion_Results" in line:
                folder_exists = True
        f.close()
        if not(folder_exists):
            os.system(" mkdir Quaternion_Results")
    def putAway(self,list,lim):
            import pickle
            pickle.dump( list , open("Quaternion_Results/" + str(lim) + ".p", "wb") )
    def get(self,lim):
        if not(self.exists(lim)):
            print "Error. Those data do not exist." 
        else:
            import pickle
            a = pickle.load( open( "Quaternion_Results/" + str(lim) + ".p", "rb" ) )
            return a
    def exists(self,lim):
        '''Checks if a certain data set exists'''
        import os
        os.system(" rm SF18_Helper.txt")
        os.system(" ls Quaternion_Results >> SF18_Helper.txt")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        f=open(dir_path + "/SF18_Helper.txt","r")
        is_There = False
        for line in f:
            if str(lim) + ".p" in line:
                is_There = True
        return is_There
    def run(self, limit):
        '''Runs tests on all Pythagorean quintuples that fit 
        within the cube with side length of limit. Pickles the results.'''
        import pickle
        allPythQuadruplesAsLists = Quadruple.findHurwitzPythagoreans(limit)
        allQuadruples = Quadruple.convert( allPythQuadruplesAsLists )
        allGenLists = GenList.findAll(limit)
        allFormulas = Formula.everyFormula()
        for f in allFormulas:
            for g in allGenLists:
                quad = f.actUpon(g)
                for q in allQuadruples:
                    if q==quad:
                        f.makeFriends(q, g)
                        g.makeFriends(q, f)
                        q.makeFriends(f, g)
        self.putAway([allFormulas, allGenLists, allQuadruples ] , limit)
def main(limit):
    '''Fast access to the run method'''
    m = Manager()
    m.run(limit)

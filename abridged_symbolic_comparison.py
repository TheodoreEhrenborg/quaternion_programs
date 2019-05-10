class Quaternion_2:
    '''A Hamiltonian of the form a+bi+cj+dk '''
    def __init__(self, a=0, b=0, c=0, d=0):
        import math 
        self.__a=float(a)
        self.__b=float(b)
        self.__c=float(c)
        self.__d=float(d)
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def get_d(self):
        return self.__d
    def get_tuple(self):
        return ( self.get_a(), self.get_b(), self.get_c(), self.get_d() )
    def get_conjugate(self):
        return Quaternion_2( self.get_a(), - self.get_b(),  - self.get_c(), - self.get_d() )
    def get_norm(self):
        return self.get_a()**2+self.get_b()**2+self.get_c()**2+self.get_d()**2
    def get_modulus(self):
        import math
        return math.sqrt( self.get_norm() )
    def __add__(self,other):
        other=self.convert(other)
        return Quaternion(self.get_a()+other.get_a(),self.get_b()+other.get_b(), self.get_c()+other.get_c(),self.get_d()+other.get_d())
    def __eq__(self,other):
        return str(self) == str(other)
    def __ne__(self,other):
        return not( self == other )
    def __repr__(self):
        return 'Quaternion_2('+str(self.get_a())+','+str(self.get_b())+','+str(self.get_c())+','+str(self.get_d())+')'
    def __str__(self):
        return self.__repr__()        
    def __radd__(self,other):
        return self+other
    def __mul__(self,other):
        other=self.convert(other)
        return Quaternion_2(self.get_a()*other.get_a()-self.get_b()*other.get_b()-self.get_c()*other.get_c()-self.get_d()*other.get_d(), self.get_a()*other.get_b()+self.get_b()*other.get_a()+self.get_c()*other.get_d()-self.get_d()*other.get_c(), self.get_a()*other.get_c()+self.get_c()*other.get_a()+self.get_d()*other.get_b()-self.get_b()*other.get_d(), self.get_a()*other.get_d()+self.get_d()*other.get_a()+self.get_b()*other.get_c()-self.get_c()*other.get_b())
    def convert(self,other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, long):
            return Quaternion_2(other,0,0,0)
        if isinstance(other, complex):
            return Quaternion_2(other.real,other.imag,0,0)
        if isinstance(other, Quaternion_2):
            return other
        else:
            raise Exception('Could not convert other')
    def __rmul__(self,other):
        other=self.convert(other)
        return other*self
    def __neg__(self):
        return -1*self
    def __sub__(self,other):
        other=self.convert(other)
        return self+-other
    def __rsub__(self,other):
        other=self.convert(other)
        return -self+other
    def __div__(self,other):
        other=self.convert(other)
        r=self*(2*other.a-other)*(1/other.modulus**2)
        return Quaternion_2(round(r.get_a(),10), round(r.get_b(),10), round(r.get_c(),10), round(r.get_d(),10))
    def __rdiv__(self,other):
        other=self.convert(other)
        return other/self
class Permutation:
    '''Represents a permutation. 
    Note that "1342" means 
    f(1) = 1, f(2) = 3, f(3) = 4, f(4) = 2. 
    It has nothing to do with indices. '''
    def __init__(self, starter = None):
        '''Enter the starter as a string in the form of "1342".
           Enter the starter as a tuple in the form of 
           (1, 13, 5, 3, 12, 9, 6, 2, 10, 11, 4, 0, 7, 8, 14)
           Yes, you can enter a list in the starter slot.'''
        self.__perm = []
        for x in starter:
            self.__perm.append( int(x) )
        self.__perm = tuple(self.__perm)
        if set(self.__perm) != set(range(1, len(self) + 1)):
            raise Exception("This Permutation was not input in the right format.")
    def __len__(self):
        return len(self.__perm)
    def get_perm_tuple(self):
        return self.__perm
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        return "Permutation(" + str(self.__perm) + ")"
    def apply(self, thing):
        if type(thing) is str:
            thing = int(thing)
        if type(thing) is chr:
            thing = int(thing)
        if type(thing) is int:
            return self.get_perm_tuple()[thing-1]
        if isinstance( thing, Permutation):
            if len(thing) != len(self):
                raise Exception("The Permutations don't have the same length.")
            temp = []
            for x in range(1, len(self) + 1):
                temp.append( self.apply( thing.apply(x) ) )
            return Permutation(temp)
        else:
            raise Exception("The Permutation could not be applied to the input.")
    def inverse(self):
        temp = range( 2*len(self), 3*len(self) ) #The high numbers will cause an error if the next lines are wrong.
        for input_num in range(1, len(self) + 1):
            output_num = self.apply(input_num)
            temp[output_num - 1] = input_num
        return Permutation(temp)
    def identity(self):
        return Permutation( range(1, len(self) + 1) )
    def __eq__(self, other):
        if not(isinstance( other , Permutation)): 
            return False
        if len(other) != len(self):
            raise Exception("The Permutations don't have the same length.")
        return str(self) == str(other)
    def __ne__(self, other):
        return not( self == other)
    def __mul__(self, other):
        '''f*g*i is the same as f(g(i))'''
        return self.apply(other)
    def __pow__(self, other):
        '''Other should be a nonnegative integer'''
        i = self.identity()
        for x in range(other):
            i = i * self
        return i
    @classmethod
    def get_all(cls,n):
        '''Returns a tuple of all Permutations of 
        length n'''
        prior = Permutation.__add_more( range(1,n+1) )
        result = ()
        for x in prior:
            result += ( Permutation(x) ,)
        return result
    @classmethod
    def __add_more(cls, whats_left ):
        '''Recursive method that helps get_all'''
        result = []
        if len(whats_left) == 1:
            result.append( whats_left ) 
        else:
            for x in whats_left:
                copy = whats_left[:]
                copy.remove(x)
                prior = Permutation.__add_more( copy )
                for small_list in prior:
                    result.append( small_list + [x] )
        return result  
class Signed_Permutation(Permutation):
    '''Represents a signed permutation. 
    Note that "[1, 3, -4, 2]" means 
    f(1) = 1, f(2) = -3, f(3) = -4, f(4) = 2. 
    It has nothing to do with indices. '''
    def __init__(self, starter = None):
        '''Enter the starter in the form of 
           (1, -13, -5, -3, 12, -9, -6, 2, -10, -11, 4, -0, 7, -8, 14)
           Yes, you can enter a list in the starter slot.'''
        new = []
        for x in starter:
            new.append( int(x) )
        self.__signed = tuple(new)
        positive_list = []
        for x in self.__signed:
            positive_list.append(abs(x))
        Permutation.__init__(self, positive_list)
    def get_signed_tuple(self):
        return self.__signed
    def __repr__(self):
        return "Signed_Permutation(" + str(self.__signed) + ")"
    def apply(self, thing):
        if type(thing) is str:
            thing = int(thing)
        if type(thing) is chr:
            thing = int(thing)
        if type(thing) is float:
            thing = int(thing)
        if type(thing) is int:
            k = 1
            if thing<0:
                k = -1
            return k * self.get_signed_tuple()[abs(thing)-1]
        if isinstance( thing, Signed_Permutation):
            if len(thing) != len(self):
                raise Exception("The Signed_Permutations don't have the same length.")
            temp = []
            for x in range(1, len(self) + 1):
                temp.append( self.apply( thing.apply(x) ) )
            return Signed_Permutation(temp)
        else:
            raise Exception("The Signed_Permutation could not be applied to the input, since the input is of type " + str(type(thing)))          
    def __eq__(self, other):
        if not(isinstance( other , Signed_Permutation)): 
            return False
        if len(other) != len(self):
            raise Exception("The Signed_Permutations don't have the same length.")
        return str(self) == str(other)            
    def identity(self):
        return Signed_Permutation( range(1, len(self) + 1) )            
    def inverse(self):
        temp = range( 2*len(self), 3*len(self) ) #The high numbers will cause an error if the next lines are wrong.
        for input_num in range(1, len(self) + 1):
            output_num = self.apply(input_num)
            k = 1
            if output_num<0:
                k = -1
            temp[abs(output_num) - 1] = input_num * k
        return Signed_Permutation(temp)
    @classmethod
    def get_all(cls,n):
        '''Returns a tuple of all Signed_Permutations of 
        length n'''
        unsigned = Permutation.get_all(n)
        unsigned_tuples = ()
        for x in unsigned:
            unsigned_tuples += ( x.get_perm_tuple(),)
        prior = Signed_Permutation.__all_signs( n )
        result = ()
        for x in prior:
            for y in unsigned_tuples:
                result += ( Signed_Permutation( Signed_Permutation.__list_multiply(x,y) ) ,)
        return result
    @classmethod
    def __all_signs(cls, n ):
        '''Recursive method. When n is 2, it returns 
        ( (1,1), (1,-1), (-1,-1), (-1,1) )''' 
        result = []
        if n == 1:
            return ( (1,) , (-1,) )  
        else:
            for x in ( 1 , -1 ):
                prior = Signed_Permutation.__all_signs( n-1 )
                for small_list in prior:
                    result.append( small_list + (x,) )
        return result
    @classmethod
    def __list_multiply(cls,a,b):
        '''a = [1,2,3] and b = [2,3,4]
        Result: [2,6,12]'''
        if len(a) != len(b):
            raise Exception("a and b are not the same length.")
        new = range( len(a) )
        for i in range( len(a) ):
            new[i] = a[i] * b[i]
        return new
    @classmethod
    def get_most(cls,n):
        '''Returns a tuple of all Signed_Permutations of 
        length n, as long as the first term of the Signed Permutation
        is +1'''
        old = cls.get_all(n)
        new = []
        for x in old:
            if x.get_signed_tuple()[0] == 1:
                new.append(x)
        return tuple(new)
class Small_Transformation:
    '''A transformation that can be applied to a Signed_Permutation.
    It creates itself based on a multiplication by a quaternion on 
    either/both sides.'''
    def __init__(self, left_factor, right_factor, scalar = 1):
        result = scalar * left_factor * Quaternion_2(1,2,3,4) * right_factor
        #result can't be a permutation because result works on the indices
        temp =  result.get_tuple() 
        self.__signs = [1,1,1,1]
        for i in range(4):
            if temp[i]<0:
                self.__signs[i] = -1
        self.__positive = []
        for x in temp:
            self.__positive.append(abs(x))
    def apply(self, other):
        start = other.get_signed_tuple()
        new = [0,0,0,0]
        for x in range(4):
            new[self.__positive.index(x+1)] = start[x]
        result = [0,0,0,0]
        for x in range(4):
            result[x] = new[x] * self.__signs[x]
        return Signed_Permutation(result)            
class Large_Transformation:
    '''A transformation that can be applied to a Product.
    It creates a list of Small_Transformation from a list of
    quaternions. For example, the list [ i, -i, j, k] tells
    it that it will operate on a Product of length 2, and it
    will do this: i * 1st factor * -1, j * 2nd factor * k.
    The default option is for the Large_Transformation to 
    create scalars for the Small_Transformations so that
    they don't change the norms of the factors of the Product.'''
    units = [ Quaternion_2(1,0,0,0), Quaternion_2(-1,0,0,0), Quaternion_2(0,1,0,0), Quaternion_2(0,-1,0,0), Quaternion_2(0,0,1,0), Quaternion_2(0,0,-1,0), Quaternion_2(0,0,0,1), Quaternion_2(0,0,0,-1) ]
    def __init__(self, quaternion_list, create_scalars = True):
        self.__quaternion_tuple = tuple(quaternion_list)
        if len( self.__quaternion_tuple ) % 2:
            raise Exception('''The length of the quaternion_list should be even
            because each factor has two sides.''')
        good = True
        for x in self.__quaternion_tuple:
            if not isinstance(x, Quaternion_2):
                good = False
        if not good:
            raise Exception("This method got a list containing something that wasn't a Quaternion_2")
        new = []
        for i in range( len( self.__quaternion_tuple ) ):
            if i%2 == 0:
                left = self.__quaternion_tuple[i]
                right = self.__quaternion_tuple[i+1]
                scalar = 1
                if create_scalars:
                    c = left*right
                    scalar = 1.0/c.get_modulus()
                new.append( Small_Transformation( left, right, scalar) )
        self.__transformation_tuple = tuple(new)
    def __repr__(self):
        return "Large_Transformation(" + str(self.__quaternion_tuple) + ")"
    def __str__(self):
        return self.__repr__()
    def apply(self, other):
        perm_tuple = other.get_perm_tuple()
        if len(perm_tuple) != len(self.__transformation_tuple):
            output = "The Large_Transformation has length " + str(len(self.__transformation_tuple))             
            output += ". The Product has length " + str(len(perm_tuple)) + "."
            raise Exception(output)
        new = []
        for i in range( len(perm_tuple) ):
            new_perm = self.__transformation_tuple[i].apply(  perm_tuple[i] )
            new.append(new_perm)
        return Product( new )
    @classmethod
    def get_ones(cls, n):
        '''Return a list of n Quaternion_2(1,0,0,0)'s'''
        result = []
        for x in range(n):
            result.append( Quaternion_2(1,0,0,0) )
        return result
    @classmethod
    def get_all_end_transformations(cls, n):
        seeds = []
        seeds.append( Quaternion_2( 1, 0, 0, 0) )
        seeds.append( Quaternion_2( -1, 0, 0, 0) )
        seeds.append( Quaternion_2( 0, 1, 0, 0) )
        seeds.append( Quaternion_2( 0, -1, 0, 0) )
        seeds.append( Quaternion_2( 0, 0, 1, 0) )
        seeds.append( Quaternion_2( 0, 0, -1, 0) )
        seeds.append( Quaternion_2( 0, 0, 0, 1) )
        seeds.append( Quaternion_2( 0, 0, 0, -1) )
        result = []
        for x in seeds:
            for y in seeds:
                temp = [x] + cls.get_ones(2*n-2) + [y]
                result.append( Large_Transformation(temp) )
        return result                
    @classmethod
    def get_all_automorphisms(cls, n):
        automorphism_seeds = []
        automorphism_seeds.append( Quaternion_2( 1, 0, 0, 0) )
        automorphism_seeds.append( Quaternion_2( 0, 1, 0, 0) )
        automorphism_seeds.append( Quaternion_2( 0, 0, 1, 0) )
        automorphism_seeds.append( Quaternion_2( 0, 0, 0, 1) )
        automorphism_seeds.append( Quaternion_2( 1, 1, 1, 1) )
        automorphism_seeds.append( Quaternion_2( 1, -1, -1, -1) )
        automorphism_seeds.append( Quaternion_2( 1, -1, 1, 1) )
        automorphism_seeds.append( Quaternion_2( 1, 1, -1, -1) )
        automorphism_seeds.append( Quaternion_2( 1, 1, -1, 1) )
        automorphism_seeds.append( Quaternion_2( 1, -1, 1, -1) )
        automorphism_seeds.append( Quaternion_2( 1, -1, -1, 1) )
        automorphism_seeds.append( Quaternion_2( 1, 1, 1, -1) )
        automorphism_seeds.append( Quaternion_2( 1, 1, 0, 0) )
        automorphism_seeds.append( Quaternion_2( 1, -1, 0, 0) )
        automorphism_seeds.append( Quaternion_2( 1, 0, 1, 0) )
        automorphism_seeds.append( Quaternion_2( 1, 0, -1, 0) )
        automorphism_seeds.append( Quaternion_2( 1, 0, 0, 1) )
        automorphism_seeds.append( Quaternion_2( 1, 0, 0, -1) )
        automorphism_seeds.append( Quaternion_2( 0, 1, 1, 0) )
        automorphism_seeds.append( Quaternion_2( 0, 1, -1, 0) )
        automorphism_seeds.append( Quaternion_2( 0, 1, 0, 1) )
        automorphism_seeds.append( Quaternion_2( 0, 1, 0, -1) )
        automorphism_seeds.append( Quaternion_2( 0, 0, 1, 1) )
        automorphism_seeds.append( Quaternion_2( 0, 0, 1, -1) )
        result = []
        for q in automorphism_seeds:
            temp = []
            for x in range(n):
                temp.append(q)
                temp.append( q.get_conjugate() )
            result.append( Large_Transformation(temp) )
        return result
    @classmethod
    def get_all_middle_transformations(cls, n):
        temp = cls.in_the_middle(n-1)
        new = []
        one = Quaternion_2(1,0,0,0)
        for x in temp:
            new.append( Large_Transformation( [one] + x + [one] ) )
        return new
    @classmethod
    def in_the_middle(cls, n ):
        '''Recursive method. It returns a list of all 
        possible lists of quaternions (with product 1) that 
        could go in the middle. When n=1, it thinks about A*B,
        so it returns 
        [ [i,-i], [-i,i], [1,1], [-1,1], [j,-j], [-j,j], [k,-k], [-k,k] ] ''' 
        result = []
        if n == 0:
            result.append( [] )
        elif n == 1:
            for x in cls.units:
                result.append( [x, x.get_conjugate() ] )
           # print result
        else:
            for x in cls.units:
                prior = cls.in_the_middle( n-1 )
            #    print prior
                for p in prior:
               #     print p
                    result.append( p + [x, x.get_conjugate() ] )
        return result
class Product:
    '''A sequence of Signed_Permutations, which represents
    something like 
    (a + b*i + c*j + d*k)(a + b*i + d*j - c*k)(a - b*i + c*j - d*k)(a + c*i + b*j + d*k) '''
    all_factors = Signed_Permutation.get_all(4)
    most_factors = Signed_Permutation.get_most(4)
    alpha = Signed_Permutation((1,2,3,4))
    alpha_bar = Signed_Permutation((1,-2,-3,-4))
    def __init__(self, perm_tuple=None, tuple_tuple_string = None, tuple_tuple = None):
        '''The presence of tuple_tuple_string overrides perm_tuple.
        The presence of tuple_tuple overrides tuple_tuple_string'''
        if tuple_tuple_string == None and tuple_tuple == None:
            self.__perm_tuple = tuple(perm_tuple)
        elif tuple_tuple == None:
            tuple_tuple = eval(tuple_tuple_string)
            self.__perm_tuple = []
            for x in tuple_tuple:
                self.__perm_tuple.append( Signed_Permutation(x) )
            self.__perm_tuple = tuple(self.__perm_tuple)
        else: 
            self.__perm_tuple = []
            for x in tuple_tuple:
                self.__perm_tuple.append( Signed_Permutation(x) )
            self.__perm_tuple = tuple(self.__perm_tuple)
        self.found = False
        self.__diary = ""
        self.__log_used = False
    def get_tuple_tuple(self):
        perm_tuple = self.get_perm_tuple()
        result = []
        for x in perm_tuple:
            result.append( x.get_signed_tuple() )
        return tuple(result)
    def is_in_most(self):
        result = True
        for x in self.get_perm_tuple():
            if x not in Product.most_factors:
                result = False
        return result
    def get_equivalents(self):
        '''Looks for any two consecutive factors
        that are conjugates. Makes a new Product
        where they have been replaced with 
        beta*beta bar, where beta is any factor with a leading +1.
        Only returns the tuple of Products one replacement
        away.'''
        t = self.get_perm_tuple()
        results = []
        for i in range(0,len(t)-1):
            first = Product( ( t[i], ) )
            second = Product( ( t[i+1], ) )
            if first.get_conjugate() == second:
                for beta in Product.most_factors:
                    beta_bar = Product( (beta,) ).get_conjugate().get_perm_tuple()[0] 
                    new = Product( t[:i] + ( beta, beta_bar ) + t[i+2:] )
                    results.append( new )
        return tuple(results)
    def log(self, info):
        if not self.was_log_used():
            self.__diary += "---------------------\n"
            self.__diary += "Log of " + str(self) + "\n"
            self.__diary += "---------------------\n"
            self.__log_used = True
        self.__diary += info
    def was_log_used(self):
        return self.__log_used
    def get_log(self):
        return self.__diary
    def is_first_one(self):
        result = True
        for perm in self.get_perm_tuple():
            if perm not in Product.most_factors:
                result = False
        return False
    def standardize(self):
        '''The first Signed_Permutation becomes the identity,
        and the others adapt.'''
        first = self.__perm_tuple[0]
        inv = first.inverse()
        new = ()
        for x in self.__perm_tuple:
            new +=  ( inv.apply(x), )
        self.__perm_tuple = new
    def get_perm_tuple(self):
        return self.__perm_tuple
    def __repr__(self):
        return "Product(" + str(self.get_perm_tuple()) + ")"
    def __str__(self):
        return self.__repr__()
    def __mul__(self,other):
        '''For example, (a + b*i + c*j + d*k) * (a + b*i + d*j - c*k)
        results in (a + b*i + c*j + d*k)(a + b*i + d*j - c*k)'''
        return Product( self.get_perm_tuple() + other.get_perm_tuple() )         
    @classmethod
    def all_products(cls, n ):
        '''Recursive method. It returns a list of all 
        possible Products (of length n) of Signed_Permutations.
        I mean all products. That is, each factor
        has 4!*2^4 possibilities, so the list will have
        length 384^n.  ''' 
        result = []
        if n == 1:
            for x in Product.all_factors:
                result.append( Product( ( x,) ) )
        else:
            for x in Product.all_factors:
                prior = Product.all_products( n-1 )
                for p in prior:
                    result.append( p * Product( (x,) ) )
        return result
    @classmethod
    def most_products(cls, n):
        '''Like all_products, but doesn't output products
        that are obviously the same. The first
        factor is always Signed_Permutation((1,2,3,4)) and 
        the first term of each factor is always +1'''
        result = []
        if n == 1:
            result.append( Product( ( Signed_Permutation( (1,2,3,4)), ) ) )
        else:
            for x in Product.most_factors:
                prior = Product.most_products( n-1 )
                for p in prior:
                    result.append( p * Product( (x,) ) )
        return result
    @classmethod
    def more_than_most_products(cls, n):
        '''Like all_products, but the first
        factor is always Signed_Permutation((1,2,3,4))'''
        result = []
        if n == 1:
            result.append( Product( ( Signed_Permutation( (1,2,3,4)), ) ) )
        else:
            for x in Product.all_factors:
                prior = Product.more_than_most_products( n-1 )
                for p in prior:
                    result.append( p * Product( (x,) ) )
        return result
    def __eq__(self,other):
        return str(self) == str(other)
    def __ne__(self,other):
        return not( self == other )
    def get_conjugate(self):
        '''The result is also flipped, as a reminder. The conjugate is an anti-automorphism.'''
        new = ()
        for x in self.get_perm_tuple():
            temp = x.get_signed_tuple()
            new_temp = (temp[0], -temp[1], -temp[2], -temp[3])
            new = ( Signed_Permutation(new_temp) ,) + new 
        result = Product( new )
        return result
    def get_copy(self):
        return Product( self.get_perm_tuple() )
    @classmethod
    def count_found(cls, product_list):
        count = 0
        for x in range(len(product_list)):
            if product_list[x].found:
                count+=1
        return count
    @classmethod
    def mark_as_found(cls, product, product_list):
        before = cls.count_found(product_list)
        for x in product_list:
            if x == product:
                x.found = True
        after = cls.count_found(product_list)
        if before != after:
            print "Increase",after-before 
def main(n=2, time_between_reports = 1800):
    '''Returns a tuple, where each element is a set of nodes 
    that lie in the same connected graph'''
    import time, random
    start_time = time.time()
    temp_count = 0
    all_products = Product.most_products(n) #Only 48^(n-1) products
    short_transformations = []
    short_transformations += Large_Transformation.get_all_automorphisms(n)
    short_transformations += Large_Transformation.get_all_middle_transformations(n)
    short_transformations += Large_Transformation.get_all_end_transformations(n)
    short_transformations += ["conjugate","equivalents"]
    print "Done creating list of transformations"
    connected = []
    for x in all_products:
        x.standardize()
        connected.append(  [x]  )
    all_products = None
    print "Done putting products in individual lists"
    while len(connected) > 1:
        checkpoint = time.time()
        while time.time() - checkpoint < time_between_reports:
            r = random.randint( 0, len(connected) - 1 )
            current_eq_class = connected.pop(r)
            r = random.randint( 0, len(current_eq_class) - 1 )
            current_product = current_eq_class[r]
            temp = None
            while temp == None or not temp.is_in_most():
                if temp == None:
                    temp = current_product
                r = random.randint( 0, len(short_transformations) - 1)
                t = short_transformations[r]
                if t == "equivalents":
                    eqs = temp.get_equivalents()
                    if len(eqs) == 0:
                        t = "conjugate"
                    else:
                        r = random.randint( 0, len(eqs) - 1)
                        temp = eqs[r]
                elif t == "conjugate":
                    temp = temp.get_conjugate()
                else:
                    temp = t.apply(temp)
                temp.standardize()
            #Now temp is in the 48^(n-1)
            if temp in current_eq_class:
                connected.append( current_eq_class )
            else:
            #Find the list in connected and add all of current_eq_class to it.
                for other_class in connected:
                    if temp in other_class:
                        break
                else:
                    raise Exception("Can't find where temp belongs. Temp = " + str(temp))
                for x in current_eq_class:
                    other_class.append(x)
        count = len(connected)
        file_name = "Results of looking for 4D "+str(n)+"-tuples starting at " + str(int(start_time))
        file_name += " with checkpoint at " + str(int(checkpoint))
        f = open(file_name, "a")
        end_time = time.time()
        f.write("This program took " + str(int(end_time - start_time)) + " seconds\n")
        f.write("\nThe program found " + str(count) + " distinct equivalence class")
        if count != 1:
            f.write("es")
        f.write("\n")
        f.write("\n\nHere's a human-readable version of the set of connected nodes.\n")
        f.write("The program does not print any products that have a permutation that doesn't start with +1\n")
        for equivalence_class in connected:
            f.write("-----------------------\n")
            for product in equivalence_class:
                p = str(product)
                if p.count("(1") == n:
                    f.write(p + "\n")
        f.write("Here's the list(s) of connected nodes:\n")
        f.write(str(connected))
        f.close()
        print "This program took " + str(int(end_time - start_time)) + " seconds\n"
        print "The program found " + str(count) + " distinct",
        if count != 1:
            print "equivalence classes"
        else:
            print "equivalence class"

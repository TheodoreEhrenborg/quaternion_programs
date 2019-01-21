'''Collects data on whether certain products of 
quaternions 'produce' the exact same solutions 
to a^2 + b^2 + c^2 + d^2 = e^n
Takes into account the fact that equivalent n-tuples
must have the same input for every output''' 
import math,time
from symbolic_comparison import Quaternion_2 as Q
betas = []
betas.append( "Q(a,b,c,d)" )
betas.append( "Q(a,b,c,-d)" )
betas.append( "Q(a,b,-c,d)" )
betas.append( "Q(a,b,-c,-d)" )
betas.append( "Q(a,-b,c,d)" )
betas.append( "Q(a,-b,c,-d)" )
betas.append( "Q(a,-b,-c,d)" )
betas.append( "Q(a,-b,-c,-d)" )
betas.append( "Q(a,b,d,c)" )
betas.append( "Q(a,b,d,-c)" )
betas.append( "Q(a,b,-d,c)" )
betas.append( "Q(a,b,-d,-c)" )
betas.append( "Q(a,-b,d,c)" )
betas.append( "Q(a,-b,d,-c)" )
betas.append( "Q(a,-b,-d,c)" )
betas.append( "Q(a,-b,-d,-c)" )
betas.append( "Q(a,c,b,d)" )
betas.append( "Q(a,c,b,-d)" )
betas.append( "Q(a,c,-b,d)" )
betas.append( "Q(a,c,-b,-d)" )
betas.append( "Q(a,-c,b,d)" )
betas.append( "Q(a,-c,b,-d)" )
betas.append( "Q(a,-c,-b,d)" )
betas.append( "Q(a,-c,-b,-d)" )
betas.append( "Q(a,c,d,b)" )
betas.append( "Q(a,c,d,-b)" )
betas.append( "Q(a,c,-d,b)" )
betas.append( "Q(a,c,-d,-b)" )
betas.append( "Q(a,-c,d,b)" )
betas.append( "Q(a,-c,d,-b)" )
betas.append( "Q(a,-c,-d,b)" )
betas.append( "Q(a,-c,-d,-b)" )
betas.append( "Q(a,d,b,c)" )
betas.append( "Q(a,d,b,-c)" )
betas.append( "Q(a,d,-b,c)" )
betas.append( "Q(a,d,-b,-c)" )
betas.append( "Q(a,-d,b,c)" )
betas.append( "Q(a,-d,b,-c)" )
betas.append( "Q(a,-d,-b,c)" )
betas.append( "Q(a,-d,-b,-c)" )
betas.append( "Q(a,d,c,b)" )
betas.append( "Q(a,d,c,-b)" )
betas.append( "Q(a,d,-c,b)" )
betas.append( "Q(a,d,-c,-b)" )
betas.append( "Q(a,-d,c,b)" )
betas.append( "Q(a,-d,c,-b)" )
betas.append( "Q(a,-d,-c,b)" )
betas.append( "Q(a,-d,-c,-b)" )
#print len( set(betas) )
def all_coordinates( n ):
    '''If n = 2, returns the
    48*48 ordered pairs whose
    coordinates range from 0 to 47'''
    result = []
    if n == 0:
        return ( (), )  
    else:
        for x in range(48):
            prior = all_coordinates( n-1 )
            for small_list in prior:
                result.append( small_list + (x,) )
    return result
def all_variants( input_list ):
    '''Given a list of 4 numbers, returns
    the 384=2^4 * 4! lists after every signed permutation
    has been applied'''
    unsigned_tuples = add_more( list(input_list) )
    #print unsigned_tuples
#    print len( input_list )
    prior = all_signs( len(input_list) )
    #print prior
    result = ()
    for x in prior:
        for y in unsigned_tuples:
            result += (  tuple(list_multiply(x,y))  ,)
    return result
def list_multiply(a,b):
    '''a = [1,2,3] and b = [2,3,4]
    Result: [2,6,12]'''
    if len(a) != len(b):
        raise Exception("a and b are not the same length.")
    new = range( len(a) )
    for i in range( len(a) ):
        new[i] = a[i] * b[i]
    return new
def all_signs( n ):
    '''Recursive method. When n is 2, it returns 
    ( (1,1), (1,-1), (-1,-1), (-1,1) )''' 
    result = []
    if n == 0:
        return ( (), ) 
    else:
        for x in ( 1 , -1 ):
            prior = all_signs( n-1 )
            for small_list in prior:
                result.append( small_list + (x,) )
    return result
def add_more(whats_left ):
    '''Recursive method that helps get_all'''
    result = []
    if len(whats_left) == 1:
        result.append( whats_left ) 
    else:
        for x in whats_left:
            copy = whats_left[:]
            copy.remove(x)
            prior = add_more( copy )
            for small_list in prior:
                result.append( small_list + [x] )
    return result
def main(how_far = 5, how_many_factors = 2, file_name = None, alternate = None ):
    n = how_many_factors
    m = how_far
    start = time.time()
    if file_name == None:
        file_name = "starting at " + str(int(start))
    '''This program writes most of its output to a file'''   
    results = {}
    for coord in all_coordinates(n-1):
        key = betas[0]
        for i in coord:
            key += "*" + betas[i]
        results[key] = set()
#    print len(results)
    if alternate != None:
        results = {}
        for key in alternate:
            results[key] = set()
    for x in range(0,m):
        for y in range(x,m):
            for z in range(y,m):
                for w in range(z,m):
                    only = [x,y,z,w]
                    for l in set(all_variants( only )):
                        for p in results.keys():
                            a = l[0]
                            b = l[1]
                            c = l[2]
                            d = l[3]
                            product = eval( p )
                            coefficients = [abs(product.get_a()), abs(product.get_b()), 
                                                    abs(product.get_c()), abs(product.get_d())]
                            coefficients.sort()
                            results[p].add(tuple(only+coefficients))
    total = set()
    unique = {}
    for x in results.keys():
        total = total | results[x]
        if results[x] not in unique.values():
            unique[x] = results[x]
    f = open("Results of looking for " + str(n) + "-tuples " + file_name, "a") 
    f.write("\n\n")
    if alternate != None:
        f.write("An alternate list was used.\n")
    f.write("This program tried to count the number of 4D " + str(n) + "-tuples" + "\n")
    f.write("This program searched over all factors whose greatest term in absolute value was " + str(m)+"\n")
    f.write("There are "+str(len(unique.keys())) +" equivalence classes that look different." + "\n")
    f.write("Here is a representative from each equivalence class:\n")
    for x in unique.keys():
        count = 0
        for i in results.keys():
            if unique[x] == results[i]:
                count += 1
        f.write(str(x) + " Frequency: " + str(count) + "\n")
    current_time = time.time()
    f.write("This program took "+ str(current_time - start) + " seconds" + "\n")
    f.write("This program considered " + str(len(total)) + " different solutions to the Diophantine equation." + "\n")
    for Y in unique.keys():
        for Z in unique.keys():
            if Y != Z:
                f.write("Here are the values of "+ Y +" that " + Z + " does not have:" + "\n")
                f.write(str(unique[Y] - unique[Z]) + "\n")
                f.write("Here are the values of "+ Z +" that " + Y + " does not have:" + "\n")
                f.write(str(unique[Z] - unique[Y]) + "\n")
    if alternate != None:
        f.write("Here's the alternate list that was used:\n")
        f.write( str( alternate ) )
        f.write("\n\n")
        for x in results.keys():
            for y in unique.keys():
                if results[x] == unique[y]:
                    if x != y:
                        f.write("Interesting: ")
                    f.write( x + " simeq " + y + "\n" )
    f.close()
    print
    if alternate != None:
        print "An alternate list was used.\n"
    print "This program tried to count the number of 4D " + str(n) + "-tuples"
    print "This program searched over all factors whose greatest term in absolute value was < " + str(m)
    print "There are "+str(len(unique.keys())) +" equivalence classes that look different."
    print "This program took", current_time - start, "seconds"
    print "This program considered " + str(len(total)) + " different solutions to the Diophantine equation."

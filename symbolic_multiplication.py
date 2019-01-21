'''Takes quaternion products and puts them
in a format that Mathematica can handle. Then 
it takes the results and puts in a human-readable
format.'''
import math,time,os
from quaternion import i,j,k
i=i()
j=j()
k=k()
def get_products():
    '''Returns the 48 quaternion products (as 2 factors) as a list of strings'''
#    start = time.time()
    alpha = "a + b*i + c*j + d*k"
    #I'm going to switch around b,c,d, then change the signs on the small scale
    beta1 = "a + b*i + c*j + d*k"
    beta2 = "a + b*i + c*j - d*k"
    beta3 = "a + b*i - c*j + d*k"
    beta4 = "a + b*i - c*j - d*k"
    beta5 = "a - b*i + c*j + d*k"
    beta6 = "a - b*i + c*j - d*k"
    beta7 = "a - b*i - c*j + d*k"
    beta8 = "a - b*i - c*j - d*k"
    beta9 = "a + b*i + d*j + c*k"
    beta10 = "a + b*i + d*j - c*k"
    beta11 = "a + b*i - d*j + c*k"
    beta12 = "a + b*i - d*j - c*k"
    beta13 = "a - b*i + d*j + c*k"
    beta14 = "a - b*i + d*j - c*k"
    beta15 = "a - b*i - d*j + c*k"
    beta16 = "a - b*i - d*j - c*k"
    beta17 = "a + c*i + b*j + d*k"
    beta18 = "a + c*i + b*j - d*k"
    beta19 = "a + c*i - b*j + d*k"
    beta20 = "a + c*i - b*j - d*k"
    beta21 = "a - c*i + b*j + d*k"
    beta22 = "a - c*i + b*j - d*k"
    beta23 = "a - c*i - b*j + d*k"
    beta24 = "a - c*i - b*j - d*k"
    beta25 = "a + c*i + d*j + b*k"
    beta26 = "a + c*i + d*j - b*k"
    beta27 = "a + c*i - d*j + b*k"
    beta28 = "a + c*i - d*j - b*k"
    beta29 = "a - c*i + d*j + b*k"
    beta30 = "a - c*i + d*j - b*k"
    beta31 = "a - c*i - d*j + b*k"
    beta32 = "a - c*i - d*j - b*k"
    beta33 = "a + d*i + b*j + c*k"
    beta34 = "a + d*i + b*j - c*k"
    beta35 = "a + d*i - b*j + c*k"
    beta36 = "a + d*i - b*j - c*k"
    beta37 = "a - d*i + b*j + c*k"
    beta38 = "a - d*i + b*j - c*k"
    beta39 = "a - d*i - b*j + c*k"
    beta40 = "a - d*i - b*j - c*k"
    beta41 = "a + d*i + c*j + b*k"
    beta42 = "a + d*i + c*j - b*k"
    beta43 = "a + d*i - c*j + b*k"
    beta44 = "a + d*i - c*j - b*k"
    beta45 = "a - d*i + c*j + b*k"
    beta46 = "a - d*i + c*j - b*k"
    beta47 = "a - d*i - c*j + b*k"
    beta48 = "a - d*i - c*j - b*k"
##    beta49 = "a + d*i - c*j - b*k"
##    listA = []
##    for x in range(1,49+1):
##        current_beta = eval("beta" + str(x))
##        print "beta" + str(x), current_beta
##        if current_beta in listA:
##            print "PROBLEM"
##        listA.append(current_beta)
###Previous code was intended to test whether all the betas were distinct. 
###It seems that they are.  
    listA = []
    for x in range(1,48+1):
        current_beta = eval("beta" + str(x))
        factors = "(" + alpha + ")(" + current_beta + ")"
##        print "product " + str(x), product
        listA.append(factors)
    return listA
def to_Mathematica_48():
    '''Returns the 48 quaternion products in a form that Mathematica can symbolically multiply'''
    listA = get_products()
    listB = [] #listB will not have blank space
    for x in listA:
        listB.append(x.replace(" ",""))
    listC = [] #listC contains the 48*4 individual coefficients. The rearrangement of multiplication has been done with strings
    for x in listB:
#        print x
        x_1 = "a" #The x_i are the variables and their sign
        x_2 = x[2:4]
        x_3 = x[6:8]
        x_4 = x[10:12]
        x_5 = "a"
        x_6 = x[17:19]
        x_7 = x[21:23]
        x_8 = x[25:27]
#        print x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8
        listC.append( "("+x_1+")("+x_5+") - ("+x_2+")("+x_6+") - ("+x_3+")("+x_7+") - ("+x_4+")("+x_8+")" )
        listC.append( "("+x_1+")("+x_6+") + ("+x_2+")("+x_5+") + ("+x_3+")("+x_8+") - ("+x_4+")("+x_7+")" )
        listC.append( "("+x_1+")("+x_7+") - ("+x_2+")("+x_8+") + ("+x_3+")("+x_5+") + ("+x_4+")("+x_6+")" )
        listC.append( "("+x_1+")("+x_8+") + ("+x_2+")("+x_7+") - ("+x_3+")("+x_6+") + ("+x_4+")("+x_5+")" )
    output = "{"#In Mathematica, lists have braces
    for x in listC:
        output += x + "," #Build the list as a string
    output = output[:-1]
    output += "}"
    print output
def from_Mathematica_48(long_string):
    '''Takes the output from Mathematica (as a long string)
    and turns it into readable quaternion identities'''
    long_string = "['" + long_string[1:-1] + "']"#The list is a string right now, so replace the braces with brackets...
    long_string = long_string.replace(",", "','")#Add extra quote marks to make it a list of strings
    long_string = long_string.replace("\n", "")#Take out the new lines
    long_list = eval(long_string) #Make the list
    for x in range(0,len(long_list)):
        long_list[x] = long_list[x].strip() #Take away the white space before and after each element
#    print long_list
    listA = get_products() 
    for x in range(0,48): #Print the 48 quaternion identities, formatted nicely
        print "Product",str(x+1) + ":"
        print format(listA[x])
        print "= " + format("(" + long_list[4*x] + ") + ("+long_list[4*x+1] + ")i + (" + long_list[4*x+2] + ")j + (" + long_list[4*x+3] + ")k")
        print
def format(y):
    return y.replace("*","").replace(" ","").replace("-"," - ").replace("+"," + ").replace("( - ","(-")
def multiply():
    '''Calculates (x_1 + x_2 * i + x_3 * j + x_4 * k)(x_5 + x_6 * i + x_7 * j + x_8 * k)              
    where the x_i can be variable expressions that Sage can handle. Is user-friendly '''
    print '''Calculates (x_1 + x_2 * i +x_3 * j + x_4 * k)(x_5 + x_6 * i + x_7 * j + x_8 * k)
    where the x_i can be variable expressions that Sage can handle ''' 
    x_1 = raw_input("x_1 = ")
    x_2 = raw_input("x_2 = ")
    x_3 = raw_input("x_3 = ")
    x_4 = raw_input("x_4 = ")
    x_5 = raw_input("x_5 = ")
    x_6 = raw_input("x_6 = ")
    x_7 = raw_input("x_7 = ")
    x_8 = raw_input("x_8 = ")
    print compute(x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8)
def compute(x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8, simple = False):
    listC = []
    listC.append( "("+x_1+")*("+x_5+") - ("+x_2+")*("+x_6+") - ("+x_3+")*("+x_7+") - ("+x_4+")*("+x_8+")" )
    listC.append( "("+x_1+")*("+x_6+") + ("+x_2+")*("+x_5+") + ("+x_3+")*("+x_8+") - ("+x_4+")*("+x_7+")" )
    listC.append( "("+x_1+")*("+x_7+") - ("+x_2+")*("+x_8+") + ("+x_3+")*("+x_5+") + ("+x_4+")*("+x_6+")" )
    listC.append( "("+x_1+")*("+x_8+") + ("+x_2+")*("+x_7+") - ("+x_3+")*("+x_6+") + ("+x_4+")*("+x_5+")" )
    variables = []
    for x in listC:
        variables += get_names( x )
    long_list = []
    for term in listC:
        output_string = "'"
        for x in variables:
            output_string += "var(\"" + x + "\");"
        output_string += "print factor("#In Sage, tuples have parenttheses
        output_string += term #Build the list as a string
        output_string += ")'"#The extra quote marks allow the Terminal window to process the list as one piece
        os.system("sage -c " + output_string + " > Sage_output.txt")
        #print "sage -c " + output_string + " > Sage_output.txt"
        f = open("Sage_output.txt","r")
        long_string = f.read().strip()#Get the results from Sage and remove the white space
        f.close()
#        long_string = "['" + long_string[1:-1] + "']"#The list is a string right now, so replace the parentheses with brackets...
#        long_string = long_string.replace(",", "','")#Add extra quote marks to make it a list of strings
        long_string = long_string.replace("\n", "")#Take out the new lines
        long_list.append(  long_string  )
#    long_list = eval(long_string) #Make the list
    for x in range(0,len(long_list)):
        long_list[x] = long_list[x].strip() #Take away the white space before and after each element
#    print long_list
    final_output = format("( (" + x_1 + ") + (" + x_2 + ") * i + (" + x_3 +") * j + (" + x_4 +") * k)( (" + x_5 +") + (" + x_6 + ") * i + (" + x_7 + ") * j + (" + x_8 + ") * k)" )
    final_output += "\n"
    final_output += "= " + format("(" + long_list[0] + ") + ("+long_list[1] + ")i + (" + long_list[2] + ")j + (" + long_list[3] + ")k")
    if simple:
        return long_list
    return final_output
def multiply_with_Mathematica():
    '''Calculates (x_1 + x_2 * i + x_3 * j + x_4 * k)(x_5 + x_6 * i + x_7 * j + x_8 * k)              
    where the x_i can be variable expressions that Mathematica can handle. Is user-friendly '''
    print '''Calculates (x_1 + x_2 * i +x_3 * j + x_4 * k)(x_5 + x_6 * i + x_7 * j + x_8 * k)
    where the x_i can be variable expressions that Mathematica can handle ''' 
    x_1 = raw_input("x_1 = ")
    x_2 = raw_input("x_2 = ")
    x_3 = raw_input("x_3 = ")
    x_4 = raw_input("x_4 = ")
    x_5 = raw_input("x_5 = ")
    x_6 = raw_input("x_6 = ")
    x_7 = raw_input("x_7 = ")
    x_8 = raw_input("x_8 = ")
    print compute_with_Mathematica(x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8)
def compute_with_Mathematica(x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8):
    listC = []
    listC.append( "("+x_1+")("+x_5+") - ("+x_2+")("+x_6+") - ("+x_3+")("+x_7+") - ("+x_4+")("+x_8+")" )
    listC.append( "("+x_1+")("+x_6+") + ("+x_2+")("+x_5+") + ("+x_3+")("+x_8+") - ("+x_4+")("+x_7+")" )
    listC.append( "("+x_1+")("+x_7+") - ("+x_2+")("+x_8+") + ("+x_3+")("+x_5+") + ("+x_4+")("+x_6+")" )
    listC.append( "("+x_1+")("+x_8+") + ("+x_2+")("+x_7+") - ("+x_3+")("+x_6+") + ("+x_4+")("+x_5+")" )
    output_string = "'{"#In Mathematica, lists have braces
    for x in listC:
        output_string += x + "," #Build the list as a string
    output_string = output_string[:-1]
    output_string += "}'"#The extra quote marks allow the Terminal window to process the list as one piece
    os.system("wolframscript -code " + output_string + " > Mathematica_output.txt")
    f = open("Mathematica_output.txt","r")
    long_string = f.read().strip()#Get the results from Mathematica and remove the white space
    f.close()
    long_string = "['" + long_string[1:-1] + "']"#The list is a string right now, so replace the braces with brackets...
    long_string = long_string.replace(",", "','")#Add extra quote marks to make it a list of strings
    long_string = long_string.replace("\n", "")#Take out the new lines
    long_list = eval(long_string) #Make the list
    for x in range(0,len(long_list)):
        long_list[x] = long_list[x].strip() #Take away the white space before and after each element
#    print long_list
    final_output = format("( (" + x_1 + ") + (" + x_2 + ") * i + (" + x_3 +") * j + (" + x_4 +") * k)( (" + x_5 +") + (" + x_6 + ") * i + (" + x_7 + ") * j + (" + x_8 + ") * k)" )
    final_output += "\n"
    final_output += "= " + format("(" + long_list[0] + ") + ("+long_list[1] + ")i + (" + long_list[2] + ")j + (" + long_list[3] + ")k")
    return final_output
def get_names( expression ):    
    result = [] 
    for start in range(len(expression)+1):
        for end in range(start,len(expression)+1):
            if acceptable( expression[start:end] ):
                result.append( expression[start:end] )
    return result
def acceptable( expression ):
    import string
    allowed = string.lowercase + string.uppercase + "1234567890_"
    allowed_first = string.lowercase + string.uppercase + "_"
    if expression == "":
        return False
    for x in expression:
        if x not in allowed:
            return False
    return expression[0] in allowed_first
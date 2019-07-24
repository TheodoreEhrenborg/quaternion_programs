'''Collects data on whether certain products of
quaternions 'produce' the exact same solutions
to a^2 + b^2 + c^2 + d^2 = e^2'''
import math
import time
from quaternion import i, j, k
i = i()
j = j()
k = k()
alpha = "a + b*i + c*j + d*k"
# I'm going to switch around b,c,d, then change the signs on the small scale
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


def base48(x):
    '''Returns a list [a,b,c,...,z] where x = 48^n * a + 48^(n-1) *b + ... + z
    The list is only as long as it needs to be. Conditions: x>=0, x in Z'''
    output = []
    while x > 0:
        remainder = x % 48
        output.append(remainder)
        x = x / 48
    output.reverse()
    return output


def main(n=5, how_many_factors=2, file_name=None):
    if how_many_factors == 2:
        two_tuples(n, file_name)
    elif how_many_factors == 3:
        three_tuples(n, file_name)
    elif how_many_factors == 4:
        four_tuples(n, file_name)
    else:
        raise Exception(
            "There are no methods to handle " +
            str(how_many_factors) +
            " tuples")


def old_two_tuples(n=5):
    start = time.time()
    ''' n*n is the largest norm that will be allowed for any of the factors'''
    # placeholder for alpha and betas
##    beta49 = "a + d*i - c*j - b*k"
##    listA = []
# for x in range(1,49+1):
##        current_beta = eval("beta" + str(x))
# print "beta" + str(x), current_beta
# if current_beta in listA:
# print "PROBLEM"
# listA.append(current_beta)
# Previous code was intended to test whether all the betas were distinct.
# It seems that they are.
    results = []
    for x in range(1, 49):
        results.append(set())
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            if a * a + b * b <= n * n:
                for c in range(-n, n + 1):
                    if a * a + b * b + c * c <= n * n:
                        for d in range(-n, n + 1):
                            if a * a + b * b + c * c + d * d <= n * n:
                                for x in range(1, 49):
                                    current_beta = eval("beta" + str(x))
                                    product = eval(alpha) * eval(current_beta)
# If the factors had norms of 5 or less
                                    A = product.a
                                    B = product.b
                                    C = product.c
                                    D = product.d
                                    coefficients = sorted([abs(A), abs(B),
                                                           abs(C), abs(D)])
                            # results[x-1] is the set of all products for this
                            # beta
                                    results[x - 1].add(tuple(coefficients))
                            # Note that coefficients is mutable, so it must become immutable
                            # before being added to the set
    total = set()
    unique = {}
    for x in range(1, 49):
        total = total | results[x - 1]
        if results[x - 1] not in unique.values():
            unique[x] = results[x - 1]
    keys = unique.keys()
    print
    print "This program searched over all factors that had a norm of at most", n * n
    print "The products that look different have the following labels:", keys
    for Y in range(0, len(keys)):
        for Z in range(Y + 1, len(keys)):
            y = keys[Y]
            z = keys[Z]
            if True:
                print "Here are the values of Product", y, "that Product", z, "does not have:"
                print unique[y] - unique[z]
                print "Here are the values of Product", z, "that Product", y, "does not have:"
                print unique[z] - unique[y]
    for x in keys:
        print "Here are the products that seem to be the same as Product", str(x) + ":"
        for y in range(0, len(results)):
            if results[y] == unique[x]:
                print y + 1,
        print
    print "Here's the list of products:"
    for x in range(1, 49):
        current_beta = eval("beta" + str(x))
        print str(x), "(" + alpha + ")" + "(" + current_beta + ")"
    print "This program took", time.time() - start, "seconds"
    print "This program considered", len(total), "different solutions to the Diophantine equation."


def three_tuples(n, file_name=None):
    start = time.time()
    if file_name is None:
        file_name = "starting at " + str(int(start))
    ''' n*n is the largest norm that will be allowed for any of the factors
    This program writes most of its output to a file'''
    results = []
    for x in range(1, 48 * 48 + 1):
        results.append(set())
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            if a * a + b * b <= n * n:
                for c in range(-n, n + 1):
                    if a * a + b * b + c * c <= n * n:
                        for d in range(-n, n + 1):
                            if a * a + b * b + c * c + d * d <= n * n:
                                for x in range(1, 49):
                                    for y in range(1, 49):
                                        current_beta = eval("beta" + str(x))
                                        current_gamma = eval("beta" + str(y))
                                        product = eval(
                                            alpha) * eval(current_beta) * eval(current_gamma)
# If the factors had norms of 5 or less
                                        A = product.a
                                        B = product.b
                                        C = product.c
                                        D = product.d
                                        coefficients = sorted([abs(A), abs(B),
                                                               abs(C), abs(D)])
                            # results[48*(x-1)+y-1] is the set of all products
                            # for this beta
                                        results[48 * (x - 1) + y -
                                                1].add(tuple(coefficients))
                            # Note that coefficients is mutable, so it must become immutable
                            # before being added to the set
    total = set()
    unique = {}
    for x in range(1, 48 * 48 + 1):
        total = total | results[x - 1]
        if results[x - 1] not in unique.values():
            unique[x] = results[x - 1]
    keys = unique.keys()
    f = open("Results of looking for 3-tuples " + file_name, "a")
    f.write("\n\n")
    f.write("This program searched over all factors that had a norm of at most " + str(n * n) + "\n")
    f.write("There are " + str(len(keys)) +
            " products that look different." + "\n")
    f.write(
        "The products that look different have the following labels: " +
        str(keys) +
        "\n")
    for Y in range(0, len(keys)):
        for Z in range(Y + 1, len(keys)):
            y = keys[Y]
            z = keys[Z]
            if True:
                f.write(
                    "Here are the values of Product " +
                    str(y) +
                    " that Product " +
                    str(z) +
                    " does not have:" +
                    "\n")
                f.write(str(unique[y] - unique[z]) + "\n")
                f.write(
                    "Here are the values of Product " +
                    str(z) +
                    " that Product " +
                    str(y) +
                    " does not have:" +
                    "\n")
                f.write(str(unique[z] - unique[y]) + "\n")
#    for x in keys:
#        print "Here are the products that seem to be the same as Product",str(x) + ":"
#        for y in range(0,len(results)):
#            if results[y] == unique[x]:
#                print y+1,
#        print
    f.write("Here's a list of products that seem distinct:" + "\n")
    for x in keys:
        digits = base48(x)
        while len(digits) < 2:
            digits = [0] + digits
        current_beta = eval("beta" + str(digits[0] + 1))
        current_gamma = eval("beta" + str(digits[1] + 1))
        f.write(str(x) + " (" + alpha + ")" +
                "(" + current_beta + ")" + "(" + current_gamma + ")" + "\n")
    current_time = time.time()
    f.write("This program took " + str(current_time - start) + " seconds" + "\n")
    f.write("This program considered " + str(len(total)) +
            " different solutions to the Diophantine equation." + "\n")
    f.close()
    print
    print "This program searched over all factors that had a norm of at most", n * n
    print "There are", str(len(keys)), "products that look different."
    print "This program took", current_time - start, "seconds"
    print "This program considered", len(total), "different solutions to the Diophantine equation."


def two_tuples(n, file_name=None):
    start = time.time()
    if file_name is None:
        file_name = "starting at " + str(int(start))
    ''' n*n is the largest norm that will be allowed for any of the factors
    This program writes most of its output to a file'''
    results = []
    for x in range(1, 48 + 1):
        results.append(set())
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            if a * a + b * b <= n * n:
                for c in range(-n, n + 1):
                    if a * a + b * b + c * c <= n * n:
                        for d in range(-n, n + 1):
                            if a * a + b * b + c * c + d * d <= n * n:
                                for x in range(1, 49):
                                    current_beta = eval("beta" + str(x))
                                    product = eval(alpha) * eval(current_beta)
# If the factors had norms of 5 or less
                                    A = product.a
                                    B = product.b
                                    C = product.c
                                    D = product.d
                                    coefficients = sorted([abs(A), abs(B),
                                                           abs(C), abs(D)])
                            # results[x-1] is the set of all products for this
                            # beta
                                    results[x - 1].add(tuple(coefficients))
                            # Note that coefficients is mutable, so it must become immutable
                            # before being added to the set
    total = set()
    unique = {}
    for x in range(1, 48 + 1):
        total = total | results[x - 1]
        if results[x - 1] not in unique.values():
            unique[x] = results[x - 1]
    keys = unique.keys()
    f = open("Results of looking for 2-tuples " + file_name, "a")
    f.write("\n\n")
    f.write("This program searched over all factors that had a norm of at most " + str(n * n) + "\n")
    f.write("There are " + str(len(keys)) +
            " products that look different." + "\n")
    f.write(
        "The products that look different have the following labels: " +
        str(keys) +
        "\n")
    for Y in range(0, len(keys)):
        for Z in range(Y + 1, len(keys)):
            y = keys[Y]
            z = keys[Z]
            if True:
                f.write(
                    "Here are the values of Product " +
                    str(y) +
                    " that Product " +
                    str(z) +
                    " does not have:" +
                    "\n")
                f.write(str(unique[y] - unique[z]) + "\n")
                f.write(
                    "Here are the values of Product " +
                    str(z) +
                    " that Product " +
                    str(y) +
                    " does not have:" +
                    "\n")
                f.write(str(unique[z] - unique[y]) + "\n")
#    for x in keys:
#        print "Here are the products that seem to be the same as Product",str(x) + ":"
#        for y in range(0,len(results)):
#            if results[y] == unique[x]:
#                print y+1,
#        print
    f.write("Here's a list of products that seem distinct:" + "\n")
    for x in keys:
        digits = base48(x)
        while len(digits) < 1:
            digits = [0] + digits
        current_beta = eval("beta" + str(digits[0] + 1))
        f.write(str(x) + " (" + alpha + ")" + "(" + current_beta + ")" + "\n")
    current_time = time.time()
    f.write("This program took " + str(current_time - start) + " seconds" + "\n")
    f.write("This program considered " + str(len(total)) +
            " different solutions to the Diophantine equation." + "\n")
    f.close()
    print
    print "This program searched over all factors that had a norm of at most", n * n
    print "There are", str(len(keys)), "products that look different."
    print "This program took", current_time - start, "seconds"
    print "This program considered", len(total), "different solutions to the Diophantine equation."


def four_tuples(n, file_name=None):
    start = time.time()
    if file_name is None:
        file_name = "starting at " + str(int(start))
    ''' n*n is the largest norm that will be allowed for any of the factors
    This program writes most of its output to a file'''
    results = []
    for x in range(1, 48 * 48 * 48 + 1):
        results.append(set())
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            if a * a + b * b <= n * n:
                for c in range(-n, n + 1):
                    if a * a + b * b + c * c <= n * n:
                        for d in range(-n, n + 1):
                            if a * a + b * b + c * c + d * d <= n * n:
                                for x in range(1, 49):
                                    for y in range(1, 49):
                                        for z in range(1, 49):
                                            current_beta = eval(
                                                "beta" + str(x))
                                            current_gamma = eval(
                                                "beta" + str(y))
                                            current_delta = eval(
                                                "beta" + str(z))
                                            product = eval(
                                                alpha) * eval(current_beta) * eval(current_gamma) * eval(current_delta)
# If the factors had norms of 5 or less
                                            A = product.a
                                            B = product.b
                                            C = product.c
                                            D = product.d
                                            coefficients = sorted([abs(A), abs(B),
                                                                   abs(C), abs(D)])
                            # results[stuff] is the set of all products for
                            # this beta, gamma, delta
                                            results[48 *
                                                    48 *
                                                    (x -
                                                     1) +
                                                    48 *
                                                    (y -
                                                     1) +
                                                    (z -
                                                        1)].add(tuple(coefficients))
                            # Note that coefficients is mutable, so it must become immutable
                            # before being added to the set
    total = set()
    unique = {}
    for x in range(1, 48 * 48 * 48 + 1):
        total = total | results[x - 1]
        if results[x - 1] not in unique.values():
            unique[x] = results[x - 1]
    keys = unique.keys()
    f = open("Results of looking for 4-tuples " + file_name, "a")
    f.write("\n\n")
    f.write("This program searched over all factors that had a norm of at most " + str(n * n) + "\n")
    f.write("There are " + str(len(keys)) +
            " products that look different." + "\n")
    f.write(
        "The products that look different have the following labels: " +
        str(keys) +
        "\n")
    for Y in range(0, len(keys)):
        for Z in range(Y + 1, len(keys)):
            y = keys[Y]
            z = keys[Z]
            if True:
                f.write(
                    "Here are the values of Product " +
                    str(y) +
                    " that Product " +
                    str(z) +
                    " does not have:" +
                    "\n")
                f.write(str(unique[y] - unique[z]) + "\n")
                f.write(
                    "Here are the values of Product " +
                    str(z) +
                    " that Product " +
                    str(y) +
                    " does not have:" +
                    "\n")
                f.write(str(unique[z] - unique[y]) + "\n")
#    for x in keys:
#        print "Here are the products that seem to be the same as Product",str(x) + ":"
#        for y in range(0,len(results)):
#            if results[y] == unique[x]:
#                print y+1,
#        print
    f.write("Here's a list of products that seem distinct:" + "\n")
    for x in keys:
        digits = base48(x)
        while len(digits) < 3:
            digits = [0] + digits
        current_beta = eval("beta" + str(digits[0] + 1))
        current_gamma = eval("beta" + str(digits[1] + 1))
        current_delta = eval("beta" + str(digits[2] + 1))
        f.write(str(x) + " (" + alpha + ")" + "(" + current_beta + ")" +
                "(" + current_gamma + ")" + "(" + current_delta + ")" + "\n")
    current_time = time.time()
    f.write("This program took " + str(current_time - start) + " seconds" + "\n")
    f.write("This program considered " + str(len(total)) +
            " different solutions to the Diophantine equation." + "\n")
    f.close()
    print
    print "This program searched over all factors that had a norm of at most", n * n
    print "There are", str(len(keys)), "products that look different."
    print "This program took", current_time - start, "seconds"
    print "This program considered", len(total), "different solutions to the Diophantine equation."

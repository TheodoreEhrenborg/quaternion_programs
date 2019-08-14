'''Collects data on whether certain products of
complex numbers 'produce' the exact same solutions
to a^2 + b^2 = c^n, n>=2'''
import math
import time


class ComplexAdjoined:
    '''Represents objects like 3 + 4i or 2 + 4*sqrt(-2)
       Two ComplexAdjoined objects with
       different values of m (where m is in Z-) will
       complain if they are forced to interact.'''

    def __init__(self, a, b, m):
        self.__a__ = a
        self.__b__ = b
        self.__m__ = m

    def get_a(self):
        return self.__a__

    def get_b(self):
        return self.__b__

    def get_m(self):
        return self.__m__

    def __add__(self, other):
        assert self.__m__ == other.get_m(), "These two objects aren't compatible"
        return ComplexAdjoined(self.__a__ + other.get_a(),
                               self.__b__ + other.get_b(), self.__m__)

    def __radd__(self, other):
        assert self.__m__ == other.get_m(), "These two objects aren't compatible"
        return self + other

    def __eq__(self, other):
        assert self.__m__ == other.get_m(), "These two objects aren't compatible"
        return self.__a__ == other.get_a() and self.__b__ == other.get_b()

    def __rmul__(self, other):
        assert self.__m__ == other.get_m(), "These two objects aren't compatible"
        return self * other

    def __neg__(self):
        return -1 * self

    def __sub__(self, other):
        assert self.__m__ == other.get_m(), "These two objects aren't compatible"
        return self + -other

    def __rsub__(self, other):
        assert self.__m__ == other.get_m(), "These two objects aren't compatible"
        return -self + other

    def __mul__(self, other):
        assert self.__m__ == other.get_m(), "These two objects aren't compatible"
        return ComplexAdjoined(
            self.__a__ *
            other.get_a() +
            self.__m__ *
            self.__b__ *
            other.get_b(),
            other.get_a() *
            self.__b__ +
            other.get_b() *
            self.__a__,
            self.__m__)

    def __repr__(self):
        return str(self.__a__) + " + " + str(self.__b__) + \
            " sqrt(" + str(self.__m__) + ")"


alpha = "complex(a,b)"
betas = ["complex(a,b)", "complex(a,-b)"]
new_alpha = "ComplexAdjoined(a, b, radicand)"
new_beta = "ComplexAdjoined(a, -b, radicand)"


def base2(x):
    '''Returns a list [a,b,c,...,z] where x = 2^n * a + 2^(n-1) *b + ... + z
    The list is only as long as it needs to be. Conditions: x>=0, x in Z'''
    output = []
    while x > 0:
        remainder = x % 2
        output.append(remainder)
        x = x / 2
    output.reverse()
    return output


def old_main(n=5, how_many_factors=2, file_name=None):
    num_possibilities = 2**(how_many_factors - 1)
    start = time.time()
    if file_name is None:
        file_name = "starting at " + str(int(start))
    ''' n*n is the largest norm that will be allowed for any of the factors
    This program writes most of its output to a file'''
    results = []
    for x in range(0, num_possibilities):
        results.append(set())
    for x in range(0, num_possibilities):
        coords = base2(x)
        while len(coords) < how_many_factors - 1:
            coords = [0] + coords
        for a in range(-n, n + 1):
            for b in range(-n, n + 1):
                if a * a + b * b <= n * n:
                    product = eval(alpha)
                    for y in range(0, how_many_factors - 1):
                        current_beta = betas[coords[y]]
                        product = product * eval(current_beta)
                    A = product.real
                    B = product.imag
                    coefficients = sorted([abs(A), abs(B)])
                    # results[x] is the set of all products for this beta
                    results[x].add(tuple(coefficients))
                    # Note that coefficients is mutable, so it must become immutable
                    # before being added to the set
    total = set()
    unique = {}
    for x in range(0, num_possibilities):
        total = total | results[x]
        if results[x] not in unique.values():
            unique[x] = results[x]
    keys = unique.keys()
    f = open(
        "Results of looking for 2D " +
        str(how_many_factors) +
        "-tuples " +
        file_name,
        "a")
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
    f.write("Here's the list of products:" + "\n")
    for x in range(0, num_possibilities):
        coords = base2(x)
        while len(coords) < how_many_factors - 1:
            coords = [0] + coords
        output = alpha
        for y in range(0, how_many_factors - 1):
            current_beta = betas[coords[y]]
            output = output + current_beta
        f.write(str(x) + ": " + output + "\n")
    current_time = time.time()
    f.write("This program took " + str(current_time - start) + " seconds" + "\n")
    f.write("This program considered " + str(len(total)) +
            " different solutions to the Diophantine equation." + "\n")
    f.close()
    print
    print "Results of looking for 2D " + str(how_many_factors) + "-tuples "
    print "This program searched over all factors that had a norm of at most", n * n
    print "There are", str(len(keys)), "products that look different."
    print "This program took", current_time - start, "seconds"
    print "This program considered", len(total), "different solutions to the Diophantine equation."


def main(how_far=5, how_many_factors=2,
         file_name=None, radicand=-1, quiet=False):
    num_possibilities = how_many_factors + 1
    start = time.time()
    if file_name is None:
        file_name = "starting at " + str(int(start))
    ''' how_far*how_far is the largest norm that will be allowed for any of the factors
    This program writes most of its output to a file'''
    results = []
    for x in range(0, num_possibilities):
        results.append(set())
    for x in range(0, num_possibilities):
        for a in range(-how_far, how_far + 1):
            for b in range(-how_far, how_far +
                           1):  # We could restrict b a little more based on the value of m
                if a * a + -radicand * b * b <= how_far * how_far:
                    product = ComplexAdjoined(1, 0, radicand)
                    for y in range(0, x):
                        product = product * eval(new_alpha)
                    for y in range(0, how_many_factors - x):
                        product = product * eval(new_beta)
                    A = product.get_a()
                    B = product.get_b()
                    coefficients = [abs(A), abs(B)]
                    if radicand == -1:  # A^2 + B^2 is B^2 + A^2, but A^2 + mB^2 is not B^2 + mA^2
                        coefficients.sort()
                        # results[x] is the set of all products for this beta
                    results[x].add(tuple(coefficients))
                    # Note that coefficients is mutable, so it must become immutable
                    # before being added to the set
    total = set()
    unique = {}
    for x in range(0, num_possibilities):
        total = total | results[x]
        if results[x] not in unique.values():
            unique[x] = results[x]
    keys = unique.keys()
    f = open(
        "Results of looking for 2D " +
        str(how_many_factors) +
        "-tuples where radicand = " +
        str(radicand) +
        " " +
        file_name,
        "a")
    f.write("\n\n")
    f.write("This program searched over all factors that had a norm of at most " +
            str(how_far * how_far) + "\n")
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
    f.write(
        "The first product was composed of only these multiplied together: " +
        new_alpha +
        "\n")
    f.write("The second product ended with this: " + new_beta + "\n")
    f.write("The last product had only these: " + new_beta + "\n")
    current_time = time.time()
    f.write("This program took " + str(current_time - start) + " seconds" + "\n")
    f.write("This program considered " + str(len(total)) +
            " different solutions to the Diophantine equation." + "\n")
    f.close()
    if quiet:
        return len(keys)
    else:
        print
        print "Results of looking for 2D " + str(how_many_factors) + "-tuples where radicand = " + str(radicand)
        print "This program searched over all factors that had a norm of at most", how_far * how_far
        print "There are", str(len(keys)), "products that look different."
        print "This program took", current_time - start, "seconds"
        print "This program considered", len(total), "different solutions to the Diophantine equation."

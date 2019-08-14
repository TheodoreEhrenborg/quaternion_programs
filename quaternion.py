'''Contains the Quaternion class. Also contains some possibly defective methods for factoring quaternions.'''


class Quaternion:
    '''A Hamiltonian of the form a+bi+cj+dk'''

    def __init__(self, a=0, b=0, c=0, d=0, use_list=False, l=None):
        if use_list:
            a = l[0]
            b = l[1]
            c = l[2]
            d = l[3]
        import math
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
        self.coeffient_list = [self.a, self.b, self.c, self.d]
        self.modulus = math.sqrt(a**2 + b**2 + c**2 + d**2)
        self.norm = a**2 + b**2 + c**2 + d**2
        if a == int(a) and b == int(b) and c == int(c) and d == int(d):
            self.Lipschitz = True
        else:
            self.Lipschitz = False
        if self.Lipschitz or (a + .5 == int(a + .5) and b + .5 == int(
                b + .5) and c + .5 == int(c + .5) and d + .5 == int(d + .5)):
            self.Hurwitz = True
        else:
            self.Hurwitz = False
        if a >= 0 and b >= 0 and c >= 0 and d >= 0:
            self.quadrant1 = True
        else:
            self.quadrant1 = False
        self.determine_reducible()
        self.make_set()

    def make_set(self):
        '''Don't trust this method'''
        self.set = {abs(self.a), abs(self.b), abs(self.c), abs(self.d)}
        # If a,b,c,d are not all distinct, I bet this doesn't work as intended.

    def __add__(self, other):
        other = self.convert(other)
        return Quaternion(self.a + other.a, self.b + other.b,
                          self.c + other.c, self.d + other.d)

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d:
            return True
        return False

    def __repr__(self):
        return 'Quaternion(' + str(self.a) + ',' + str(self.b) + \
            ',' + str(self.c) + ',' + str(self.d) + ')'

    def __str__(self):
        if self.modulus == 0:
            return '0'
        if self.a == int(self.a):  # No terms with .0
            a = int(self.a)
        else:
            a = self.a
        if self.b == int(self.b):
            b = int(self.b)
        else:
            b = self.b
        if self.c == int(self.c):
            c = int(self.c)
        else:
            c = self.c
        if self.d == int(self.d):
            d = int(self.d)
        else:
            d = self.d
        to_print = ''
# if a!=0:  #ERROR
# to_print+=(str(a))
# if b>0:
# to_print+=('+'+str(b))
# if b<0:
# to_print+=(str(b))
# if c>0:
# to_print+=('+'+str(c))
# if c<0:
# to_print+=(str(c))
# if d>0:
# to_print+=('+'+str(d))
# if d<0:
# to_print+=(str(d))
# return to_print
# to_print=str(a)+'+'+str(b)+'i+'+str(c)+'j+'+str(d)+'k'
        if a != 0:  # No terms with zero
            to_print += str(a)
        if b != 0:  # No terms with zero
            to_print += '+' + str(b)
            if b * b == 1:  # Remove a solitary 1
                to_print = to_print[:-1]
            to_print += 'i'
        if c != 0:  # No terms with zero
            to_print += '+' + str(c)
            if c * c == 1:  # Remove a solitary 1
                to_print = to_print[:-1]
            to_print += 'j'
        if d != 0:  # No terms with zero
            to_print += '+' + str(d)
            if d * d == 1:  # Remove a solitary 1
                to_print = to_print[:-1]
            to_print += 'k'
        if to_print[0] == '+':  # No leading +
            to_print = to_print[1:]
        new_to_print = ''
        for x in range(0, len(to_print)):  # Removes the + of +-5
            append = True
            if x != len(to_print) - 1:
                if to_print[x + 1] == '-':
                    append = False
            if append:
                new_to_print += to_print[x]
        return new_to_print

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        other = self.convert(other)
        return Quaternion(
            self.a *
            other.a -
            self.b *
            other.b -
            self.c *
            other.c -
            self.d *
            other.d,
            self.a *
            other.b +
            self.b *
            other.a +
            self.c *
            other.d -
            self.d *
            other.c,
            self.a *
            other.c +
            self.c *
            other.a +
            self.d *
            other.b -
            self.b *
            other.d,
            self.a *
            other.d +
            self.d *
            other.a +
            self.b *
            other.c -
            self.c *
            other.b)

    def convert(self, other):
        if isinstance(other, int) or isinstance(
                other, float) or isinstance(other, long):
            return Quaternion(other, 0, 0, 0)
        if isinstance(other, complex):
            return Quaternion(other.real, other.imag, 0, 0)
        if isinstance(other, Quaternion):
            return other

    def __rmul__(self, other):
        other = self.convert(other)
        return other * self

    def __neg__(self):
        return -1 * self

    def __sub__(self, other):
        other = self.convert(other)
        return self + -other

    def __rsub__(self, other):
        other = self.convert(other)
        return -self + other

    def __div__(self, other):
        other = self.convert(other)
        r = self * (2 * other.a - other) * (1 / other.modulus**2)
        return Quaternion(round(r.a, 10), round(r.b, 10),
                          round(r.c, 10), round(r.d, 10))

    def __rdiv__(self, other):
        other = self.convert(other)
        return other / self

    def jiggle(self):
        '''What does this method do?
        It looks like it randomly rearranges the coefficients.'''
        import random
        new_list = self.coeffient_list[:]
        random.shuffle(new_list)
        return Quaternion(0, 0, 0, 0, use_list=True, l=new_list)

    def determine_reducible(self):
        '''I'm not sure that this can handle half-integers or negative terms.
        \nBut maybe no methods use the reducible attribute.'''
        from mymath import gcf
        if gcf(self.a, gcf(self.b, gcf(self.c, self.d))) == 1:
            self.reducible = False
        else:
            self.reducible = True


def i():
    return Quaternion(0, 1, 0, 0)


def j():
    return Quaternion(0, 0, 1, 0)


def k():
    return Quaternion(0, 0, 0, 1)
# def pyth_factor(number):#Given a Pythagorean quintuple written as a quaternion,
# I=i()#this function attempts to factor it into two Hurwitz quaternions, both using the same numbers.
# number=I.convert(number)
# print number
##    from math import sqrt
# factors=[]
# for aa in range(0,int(2*(sqrt(number.modulus)+.5))):#Let a be nonnegative. Also, since this factorization is done
# a=float(aa)/2# over the Hurwitz quaternions, we must divide aa by 2 to get the appropriate range of numbers
# print a
# for bb in range(-int(2*(sqrt(number.modulus)+.5)),int(2*(sqrt(number.modulus)+.5))): #b,c,d, need not
# b=float(bb)/2#be nonnegative
# for cc in range(-int(2*(sqrt(number.modulus)+.5)),int(2*(sqrt(number.modulus)+.5))):
# c=float(cc)/2
# for dd in range(-int(2*(sqrt(number.modulus)+.5)),int(2*(sqrt(number.modulus)+.5))):
# d=float(dd)/2 #This method is very inefficient.
# print 6
# divisor=Quaternion(a,b,c,d)
# print 7
# if not divisor.Hurwitz:
# continue
# if divisor.norm!=number.modulus:
# continue
# quotient=number/divisor
# if quotient.Hurwitz:
# factors.append([divisor,quotient])
# print 10
# print 9
# print 8
# return factors


# Given a Pythagorean quintuple written as a quaternion,
def pyth_factor2(number, quadrant_1_only=False, jiggle=True):
    # this function attempts to factor it into two Lipschitz quaternions, both
    # using the same numbers.
    I = i()
    number = I.convert(number)
   # print number
    from math import sqrt
    factors = []
    count = 0
    if not(jiggle):
        count = 99
    test = False
    while len(factors) == 0 and count < 100:
        for aa in range(0, int(2 * (sqrt(number.modulus) + .5))
                        ):  # Let a be nonnegative. Also, since this factorization is done
            # over the Hurwitz quaternions, we must divide aa by 2 to get the
            # appropriate range of numbers
            a = float(aa) / 2
#            print a
            for bb in range(-int(2 * (sqrt(number.modulus) + .5)),
                            int(2 * (sqrt(number.modulus) + .5))):  # b,c,d, need not
                b = float(bb) / 2  # be nonnegative
                for cc in range(-int(2 * (sqrt(number.modulus) + .5)),
                                int(2 * (sqrt(number.modulus) + .5))):
                    c = float(cc) / 2
                    for dd in range(-int(2 * (sqrt(number.modulus) + .5)),
                                    int(2 * (sqrt(number.modulus) + .5))):
                        d = float(dd) / 2  # This method is very inefficient.
                        test = False
                        if (a, b, c, d) == (2, 1, 0, 0):
                            test = True
                      #  print 6
                        divisor = Quaternion(a, b, c, d)
                     #   print 7
                 #       if test:
                  #          print divisor
                    #    if divisor==2+I:
                     #       print 'here'
                        if not divisor.Lipschitz:
                            continue
                        if divisor.norm != number.modulus:
                            continue
                        quotient = number / divisor
                        if quotient.set != divisor.set:
                            continue
                        if quadrant_1_only:
                            if not(quotient.quadrant1 or divisor.quadrant1):
                                continue
               #         if test:
                #            print 'q:',quotient.coeffient_list
                        if quotient.Lipschitz:
                            factors.append([divisor, quotient])
                           # print 10
                      #  print 9
      #  print 8
        count += 1
        if jiggle:
            number = number.jiggle()
    if count == 100 and len(factors) == 0:
        print "FAILURE to factor", number, "which had a modulus of", number.modulus
    return factors
# list of 24 permutations: [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0,
# 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1], [1, 0, 2, 3], [1, 0, 3, 2], [1, 2,
# 0, 3], [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0], [2, 0, 1, 3], [2, 0, 3,
# 1], [2, 1, 0, 3], [2, 1, 3, 0], [2, 3, 0, 1], [2, 3, 1, 0], [3, 0, 1,
# 2], [3, 0, 2, 1], [3, 1, 0, 2], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1,
# 0]]


# Given a Pythagorean quintuple written as a quaternion,
def pyth_factor(number, quadrant_1_only=False, jiggle=True):
    # this function attempts to factor it into two Hurwitz quaternions, both
    # using the same numbers.
    I = i()
    number = I.convert(number)
   # print number
    from math import sqrt
    factors = []
    count = 0
    if not(jiggle):
        count = 99
    test = False
    while len(factors) == 0 and count < 100:
        for aa in range(0, int(2 * (sqrt(number.modulus) + .5))
                        ):  # Let a be nonnegative. Also, since this factorization is done
            # over the Hurwitz quaternions, we must divide aa by 2 to get the
            # appropriate range of numbers
            a = float(aa) / 2
#            print a
            for bb in range(-int(2 * (sqrt(number.modulus) + .5)),
                            int(2 * (sqrt(number.modulus) + .5))):  # b,c,d, need not
                b = float(bb) / 2  # be nonnegative
                for cc in range(-int(2 * (sqrt(number.modulus) + .5)),
                                int(2 * (sqrt(number.modulus) + .5))):
                    c = float(cc) / 2
                    for dd in range(-int(2 * (sqrt(number.modulus) + .5)),
                                    int(2 * (sqrt(number.modulus) + .5))):
                        d = float(dd) / 2  # This method is very inefficient.
                        test = False
                        if (a, b, c, d) == (2, 1, 0, 0):
                            test = True
                      #  print 6
                        divisor = Quaternion(a, b, c, d)
                     #   print 7
                 #       if test:
                  #          print divisor
                    #    if divisor==2+I:
                     #       print 'here'
                        if not divisor.Hurwitz:
                            continue
                        if divisor.norm != number.modulus:
                            continue
                        quotient = number / divisor
                        if quotient.set != divisor.set:
                            continue
                        if quadrant_1_only:
                            if not(quotient.quadrant1 or divisor.quadrant1):
                                continue
               #         if test:
                #            print 'q:',quotient.coeffient_list
                        if quotient.Hurwitz:
                            factors.append([divisor, quotient])
                           # print 10
                      #  print 9
      #  print 8
        count += 1
        if jiggle:
            number = number.jiggle()
    if count == 100 and len(factors) == 0:
        print "FAILURE to factor", number, "which had a modulus of", number.modulus
    return factors

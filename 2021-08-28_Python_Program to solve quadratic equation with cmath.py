#Python program to solve quadratic equation with cmath
# ax**2 + bx + c =0

"Computer Programming Tutor,May 19, 2021"

#1. cmath: Module for complex math module

import cmath

a =float(input("Enter a: "))
b =float(input("Enter b: "))
c =float(input("Enter c: "))

# 2. calculate the Discriminant

d = (b**2)-(4*a*c)

#3. Finding x1 & x2 Values

x1= (-b - cmath.sqrt(d))/(2*a)
x2= (-b + cmath.sqrt(d))/(2*a)

print(" The Roots are {0} and {1}".format(x1,x2))

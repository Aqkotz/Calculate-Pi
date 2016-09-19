"""
calculatepi.py
Author: Andy Kotz
Credit: Mr. Dennison
Assignment:

Write and submit a Python program that computes an approximate value of π by calculating the following sum:

(see: https://github.com/HHS-IntroProgramming/Calculate-Pi/blob/master/README.md)

This sum approaches the true value of π as n approaches ∞.

Your program must ask the user how many terms to use in the estimate of π, how many decimal places, 
then print the estimate using that many decimal places. Exactly like this:

I will estimate pi. How many terms should I use? 100
How many decimal places should I use in the result? 7
The approximate value of pi is 3.1315929


Note: remember that the printed value of pi will be an estimate!

"""
import math
terms = input("I will estimate pi. How many terms should I use? ")
decimalplaces = input("How many decimal places should I use in the result? ")
termlist = list(range(10000))
termlist = [(x*2+1)*(-1.0)**x for x in termlist]
termlist = [1/x for x in termlist]
terms = int(terms)
termlist = termlist[0:terms]
termlistval = sum(termlist)
pireal = 4*(termlistval)
decimalplaces = int(decimalplaces-1)
pirem = ((10**decimalplaces)*pireal)%1
pibig = ((10**decimalplaces)*pireal)-pirem
pi = pibig/(10**decimalplaces)
pistr = str(pi)
print("The approximate value of pi is " + pistr)
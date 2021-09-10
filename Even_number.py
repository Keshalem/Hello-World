# Program to display the Even number up to n-th term
nterms = int(input("How many terms? "))

# first term
n1 = 0
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")

# generate Even Number
else:
   print("Even Numbers are:")
   while count < nterms:
       print(n1)
       nth = n1 + 2
       # update values
       n1 = nth
       count += 1
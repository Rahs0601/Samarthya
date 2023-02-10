# Using Recursion
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
 
num = int(input("Enter a number: "))  

if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num)) 

# Without using Recursion
n=int(input("Enter number: "))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial of the number is:",fact)
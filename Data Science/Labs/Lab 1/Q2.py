import math

a= int(input())
b= int(input())
c= int(input())


D=(b*b) - (4*a*c)

if (D > 0):
    sol1= (-b + math.sqrt(D)/ (2*a))
    sol2= (-b - math.sqrt(D)/ (2*a))
    print ('the solution are {0} and {1}'.format(sol1,sol2))
    
    
elif (D==0):
    real=(-b/(2*a))
    print("Root is real {0}".format(real))
    
else:
    print("Only complex roots")
    

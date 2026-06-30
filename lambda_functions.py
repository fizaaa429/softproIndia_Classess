""" 
Lambda function - Throwaway function you 
write inline (function def ,)
"""


def square_def(n):
    return n*n

square_lambda = lambda n: n*n
print(square_def(10))
print(square_lambda(10))


add = lambda a,b: a+b
print(add (2,8))


nums = [1,2,3,4,5,6]
#map : apply a function to every item.
double = list(map(lambda n:n*2,nums))
print(double)

evens = list(filter(lambda n: n%2==0, nums))
print(evens)





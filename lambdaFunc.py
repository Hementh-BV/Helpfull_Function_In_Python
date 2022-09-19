# lambda function is also called as anonymous function
# lambda function are faster than normal func

def add(a,b):
    return a+b

print(add(10,20))


sum = lambda a,b:a+b
print(sum(10,20))

even = lambda a:a%2==0
print(even(10))

threesum = lambda a,b,c:a+b+c
print(threesum(1,2,3))

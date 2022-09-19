def evenOdd(num):
    if num % 2 == 0:
        return "The num {0} is Even".format(num)
    else:
        return "The num {} is Odd".format({num})


def even_odd(num):
    if num % 2 == 0:
        return True


print(evenOdd(10))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenodd = list(map(evenOdd, lst))
print(evenodd)

evenodd = list(filter(evenOdd, lst))
print(evenodd)

evenodd = list(map(even_odd, lst))
print(evenodd)

evenoddfilter = list(filter(even_odd, lst))
print(evenoddfilter)

even = list(filter(lambda a: a % 2 == 0, lst))
print(even)

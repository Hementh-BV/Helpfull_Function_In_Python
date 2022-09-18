# try:
#     a = int(input("Enter a number"))
#     b = int(input("Enter a number"))
#     c = a + b
#     d = a / b
# except NameError:  # a = b where b is not defined
#     print("variable b is not been defined by the user")
# except ZeroDivisionError:  # a/b where b = 0
#     print("Please provide number greater than zero")
# except TypeError:  # a + b where a = 1 and b = "s"
#     print("try to make data type similar")
# except Exception as ex:
#     print(ex)
# else:  # will execute only when no exception error occurs
#     print(c)
#     print(d)
# finally:  # will execute no matter what happens Ex: in order to close database connection
#     print("Execution is done")


# Custom Exception handling

class Error(Exception):
    pass


class dobException(Error):
    pass


year = int(input("Enter the year of Birth"))
age = 2022 - year

try:
    if age > 18 and age < 30:
        print("Age is valid")
    else:
        raise dobException

except dobException:
    print("The year is not valid")

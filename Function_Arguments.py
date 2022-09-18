
# here name is positional arguments and age is keyword arguments
def hello(name,age=22):
    return "My name is {} and Im {} years old".format({name},{age})

hello("Hemu",22)

def welcome(*args,**kwargs):
    print(args)
    print(kwargs)

#welcome("Hemu","bv",age = 22,height=172)

lst=['Hemu', 'bv']
dict={'age': 22, 'height': 172}

welcome(*lst,**dict)

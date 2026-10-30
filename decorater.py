"""Create a decorator that counts how many times a function is called.

The original function should print "Hello".


def car (namanan):
    print("1. Car taken")
    def modification():
        namanan()
        print("3.Modification started")
        print("4.Modification Ended")
    return modification
@car
def onprocess():
    print("Onprocess")
print("2.Arrived to the shed")
onprocess()"""


def func(hell):
    hell()
    
    def func1():
        hell()
        print("HELLO")
    return func1
@func
def multiple():
    for i in range(6):
        print("function call ",i)
multiple()
        
        

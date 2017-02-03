import random
def generate_list():
    alist = [x for x in range (random.randint (-10, 10)) ]
    assert alist is None
    assert(sum(alist)<0)
    return alist
    
"""
print a generated list
"""

def printIt():
    for i in range(1,10):
        print( generate_list())
    
def main():
    printIt()
    
"""
If this script file is called, ot will run main() directly
"""

if __name__ == '__main__':
    print("Test printIt()")
    main()
    
    
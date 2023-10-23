import random
def print_values():
    a=random.randint(0,10000)
    b=random.randint(0,10000)
    c=random.randint(0,10000)
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b>c:
            if a>c:
                print(b,a,c)
            else:
                print(b,c,a)
        else:
            print(c,b,a)
print_values()
def batting1(d):
    print(format("%s\'s batting started"%d,"^70"))
    s=0
    a=0
    b=1
    while(a!=b):
        a=int(input("%s\'s Run:"%d))
        if(a in [0,1,2,3,4,5,6]):
            import random
            b=random.randrange(7)
            print("Opponent\'s Ball:",b)
            if(a!=b):
                s=s+a
                print("%s\'s Score:"%d,s)
        else:
            break
    print(format("OUT","^70"))
    print(format("%s\'s Final Score:%d"%(d,s),"^70"))
    return s+1
def bowling1(d,s):
    print(format("%s\'s bowling started"%d,"^70"))
    z=0
    a=0
    b=1
    print(format("%d runs to win"%s,"^70"))
    while(s>0 and a!=b):
        if(a!=b):
            a=int(input("%s\'s Ball:"%d))
            import random
            b=random.randrange(7)
            print("Opponent\'s Run:",b)
            if(a!=b):
                z=z+b
                print("Opponent\'s Score:",z)
                s=s-b
                if(s>0):
                     print(format("%d runs to win"%s,"^70"))
            else:
                print(format("WICKET","^70"))
                print(format("Opponent\'s Final score:%d"%z,"^70"))
                print(format("%s won the match"%d,"^70"))
                break
    else:
        print(format("Opponent won the match","^70"))
def bowling2(d):
    print(format("%s\'s bowling started"%d,"^70"))
    s=0
    a=0
    b=1
    while(a!=b):
        a=int(input("%s\'s Ball:"%d))
        import random
        b=random.randrange(7)
        print("Opponent\'s Run:",b)
        if(a!=b):
            s=s+b
            print("Opponent\'s score:",s)
    print(format("WICKET","^70"))
    print(format("Opponent\'s Final score:%d"%s,"^70"))
    return s+1
def batting2(d,s):
    print(format("%s\'s batting started"%d,"^70"))
    z=0
    a=0
    b=1
    print(format("%d runs to win"%s,"^70"))
    while(s>0 and a!=b):
        if(a!=b):
            a=int(input("%s\'s Run:"%d))
            import random
            b=random.randrange(7)
            print("Opponent\'s Ball:",b)
            if(a!=b and a in [0,1,2,3,4,5,6]):
                z=z+a
                print("%s\'s score:"%d,z)
                s=s-a
                if(s>0):
                     print(format("%d runs to win"%s,"^70"))
            else:
                print(format("OUT","^70"))
                print(format("%s\'s Final score:%d"%(d,z),"^70"))
                print(format("Opponent won the match","^70"))
                break
    else:
        print(format("%s won the match"%d,"^70"))
print(format("WELCOME TO HAND CRICKET","^70"))
d=input("Enter the name:")
e=input("Enter even or odd for toss:")
f=int(input("Enter the number for toss:"))
import random
g=random.randrange(7)
print("Opponent number:",g)
h=f+g
if(h%2==0):
    print("%d is even"%h)
    if(e=="even"):
        print("You won the toss")
        i=input("Enter batting or bowling:")
        if(i=="batting"):
            print("%s selected batting first"%d)
            j=batting1(d)
            bowling1(d,j)
        else:
            print("%s selected bowling first"%d)
            k=bowling2(d)
            batting2(d,k)
    else:
        print("Opponent won the toss")
        l=random.randrange(2)
        if(l==0):
            print("Opponent selected batting first")
            k=bowling2(d)
            batting2(d,k)
        else:
            print("Opponent selected bowling first")
            j=batting1(d)
            bowling1(d,j)
else:
    print("%d is odd"%h)
    if(e=="odd"):
        print("You won the toss")
        i=input("Enter batting or bowling:")
        if(i=="batting"):
            print("%s selected batting first"%d)
            j=batting1(d)
            bowling1(d,j)
        else:
            print("%s selected bowling first"%d)
            k=bowling2(d)
            batting2(d,k)
    else:
        print("Opponent won the toss")
        l=random.randrange(2)
        if(l==0):
            print("Opponent selected batting first")
            k=bowling2(d)
            batting2(d,k)
        else:
            print("Opponent selected bowling first")
            j=batting1(d)
            bowling1(d,j)
        

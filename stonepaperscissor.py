a=input("Enter your name:")
b=["stone","paper","scissor"]
n=0
m=0
def stone(x):
    if(x=="stone"):
        return 0
    elif(x=="paper"):
        return -1
    else:
        return 1
def paper(x):
    if(x=="stone"):
        return 1
    elif(x=="paper"):
        return 0
    else:
        return -1
def scissor(x):
    if(x=="stone"):
        return -1
    elif(x=="paper"):
        return 1
    else:
        return 0    
while(n<10 and m<10):
    c=input("%s\'s turn:"%a)
    import random
    d=random.choice(b)
    print("Opponent chosen",d)
    if(c=="stone"):
        e=stone(d)
        if(e==-1):
            m=m+1
            print("%s\'s score:"%a,n)
            print("Opponent's score:",m)
        else:
            n=n+e
            print("%s\'s score:"%a,n)
            print("Opponent's score:",m)
    elif(c=="paper"):
        e=paper(d)
        if(e==-1):
            m=m+1
            print("%s\'s score:"%a,n)
            print("Opponent's score:",m)
        else:
            n=n+e
            print("%s\'s score:"%a,n)
            print("Opponent's score:",m)
    else:
        e=scissor(d)
        if(e==-1):
            m=m+1
            print("%s\'s score:"%a,n)
            print("Opponent's score:",m)
        else:
            n=n+e
            print("%s\'s score:"%a,n)
            print("Opponent's score:",m)
if(n==10):
    print(format("%s won the match"%a,"^70"))
else:
    print(format("Opponent won the match","^70"))
        
    

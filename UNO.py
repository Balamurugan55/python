import time as x
import random
def opp(z,y):
    for i in y:
        m1=i.split()
        for j in m1:
            if(j in z): 
                return i
                break
        else:
            if(i=="colour"):
                return "colour"
            elif(i=="+4"):
                return "+4"
    else:
        return "take"
def colour(x):
    r=0
    b=0
    g=0
    y=0
    for i in x:
        if("red" in i):
            r=r+1
    for j in x:
        if("blue" in j):
            b=b+1
    for k in x:
        if("green" in k):
            g=g+1
    for l in x:
        if("yellow" in l):
            y=y+1
    if(r>b and r>g and r>y):
        return "red"
    elif(b>r and b>g and b>y):
        return "blue"
    elif(g>r and g>b and g>y):
        return "green"
    else:
        return "yellow"
a=input("Enter your name:")
b=input("Enter the first opponent name:")
c=input("Enter the second opponent name:")
d=input("Enter the third opponent name:")
e=["red 1","blue 1","green 1","yellow 1","red 1","blue 1","green 1","yellow 1","red 2","blue 2","green 2","yellow 2","red 2","blue 2","green 2","yellow 2","red 3","blue 3","green 3","yellow 3","red 3","blue 3","green 3","yellow 3","red 4","blue 4","green 4","yellow 4","red 4","blue 4","green 4","yellow 4","red 5","blue 5","green 5","yellow 5","red 5","blue 5","green 5","yellow 5","red 6","blue 6","green 6","yellow 6","red 6","blue 6","green 6","yellow 6","red 7","blue 7","green 7","yellow 7","red 7","blue 7","green 7","yellow 7","red 8","blue 8","green 8","yellow 8","red 8","blue 8","green 8","yellow 8","red 9","blue 9","green 9","yellow 9","red 9","blue 9","green 9","yellow 9","red 0","blue 0","green 0","yellow 0","red 0","blue 0","green 0","yellow 0","red +2","blue +2","green +2","yellow +2","red +2","blue +2","green +2","yellow +2","red skip","blue skip","green skip","yellow skip","red skip","blue skip","green skip","yellow skip","red turn","blue turn","green turn","yellow turn","red turn","blue turn","green turn","yellow turn","colour","colour","colour","colour","+4","+4","+4","+4"]
a1=[]
import random
for i in range(7):
    d2=random.choice(e)
    a1.append(d2)
    e.remove(d2)
b1=[]
import random
for i in range(7):
    d2=random.choice(e)
    b1.append(d2)
    e.remove(d2)
c1=[]
import random
for i in range(7):
    d2=random.choice(e)
    c1.append(d2)
    e.remove(d2)
d1=[]
import random
for i in range(7):
    d2=random.choice(e)
    d1.append(d2)
    e.remove(d2)
h=random.randrange(1,5)
z=random.choice(e)
t=["blue","green","yellow","red"]
if(z=="colour" or z=="+4"):
    z=random.choice(t)
print("first card:",z)
j=0
f1=""
while True:
    if h==1:
        y=random.randrange(6)
        x.sleep(y)
        print("%s\'s cards:"%a,a1)
        f1=input("%s select a card:"%a)
        if f1 not in ["colour","+4","take"]:
            if(f1 in a1):
                g1=z.split()
                for i in g1:
                    if (i in f1):
                        z=f1
                        e.append(f1)
                        a1.remove(f1)
                        if("+2" in f1):
                            if (j==0):
                                for i in range(2):
                                    d3=random.choice(e)
                                    b1.append(d3)
                                    e.remove(d3)
                                print("%s taken two cards"%b)
                            else:
                                for i in range(2):
                                    d3=random.choice(e)
                                    d1.append(d3)
                                    e.remove(d3)
                                print("%s taken two cards"%d)
                            if(j==0):
                                h=2
                            else:
                                h=4
                            break
                        elif("turn" in f1):
                            if(j==0):
                                j=1
                                print("%s turned the game"%a)
                            else:
                                j=0
                                print("%s turned the game"%a)
                            break
                        elif("skip" in f1):
                            if(j==0):
                                h=2
                                print("%s\'s chance skipped"%b)
                            else:
                                h=4
                                print("%s\'s chance skipped"%d)
                            break
                        else:
                            break
        elif("colour" in f1):
            k=input("%s select colour:"%a)
            if(k=="red"):
                z="red"
            elif(k=="blue"):
                z="blue"
            elif(k=="green"):
                z="green"
            elif(k=="yellow"):
                z="yellow"
            e.append(f1)
            a1.remove(f1)
        elif("+4" in f1):
            k=input("%s select colour:"%a)
            if(k=="red"):
                z="red"
            elif(k=="blue"):
                z="blue"
            elif(k=="green"):
                z="green"
            elif(k=="yellow"):
                z="yellow"
            if (j==0):
                for i in range(4):
                    d3=random.choice(e)
                    b1.append(d3)
                    e.remove(d3)
                print("%s taken four cards"%b)
            else:
                for i in range(4):
                    d3=random.choice(e)
                    d1.append(d3)
                    e.remove(d3)
                print("%s taken four cards"%d)
            if(j==0):
                h=2
            else:
                h=4
        else:
            d4=random.choice(e)
            a1.append(d4)
            e.remove(d4)
            print("%s taken a card:"%a,d4)
            f1=d4
            if f1 not in ["colour","+4"]:
                if(f1 in a1):
                    g1=z.split()
                    for i in g1:
                        if(i in f1):
                            print("%s kept the taken card:"%a,f1)
                            z=f1
                            e.append(f1)
                            a1.remove(f1)
                            if("+2" in f1):
                                if (j==0):
                                    for i in range(2):
                                        d3=random.choice(e)
                                        b1.append(d3)
                                        e.remove(d3)
                                    print("%s taken two cards"%b)
                                else:
                                    for i in range(2):
                                        d3=random.choice(e)
                                        d1.append(d3)
                                        e.remove(d3)
                                    print("%s taken two cards"%d)
                                if(j==0):
                                    h=2
                                else:
                                    h=4
                                break
                            elif("turn" in f1):
                                if(j==0):
                                    j=1
                                    print("%s turned the game"%a)
                                else:
                                    j=0
                                    print("%s turned the game"%a)
                                break
                            elif("skip" in f1):
                                if(j==0):
                                    h=2
                                    print("%s\'s chance skipped"%b)
                                else:
                                    h=4
                                    print("%s\'s chance skipped"%d)
                                break
                            else:
                                break
            elif("colour" in f1):
                print("%s kept the taken card:"%a,f1)
                k=input("%s select colour:"%a)
                if(k=="red"):
                    z="red"
                elif(k=="blue"):
                    z="blue"
                elif(k=="green"):
                    z="green"
                elif(k=="yellow"):
                    z="yellow"
                e.append(f1)
                a1.remove(f1)
            elif("+4" in f1):
                print("%s kept the taken card:"%a,f1)
                k=input("%s select colour:"%a)
                if(k=="red"):
                    z="red"
                elif(k=="blue"):
                    z="blue"
                elif(k=="green"):
                    z="green"
                elif(k=="yellow"):
                    z="yellow"
                if (j==0):
                    for i in range(4):
                        d3=random.choice(e)
                        b1.append(d3)
                        e.remove(d3)
                    print("%s taken four cards"%b)
                else:
                    for i in range(4):
                        d3=random.choice(e)
                        d1.append(d3)
                        e.remove(d3)
                    print("%s taken four cards"%d)
                if(j==0):
                    h=2
                else:
                    h=4
                e.append(f1)
                a1.remove(f1)
        l=len(a1)
        if(l==1):
            print("%s said UNO"%a)
        elif(l==0):
            break
    elif h==2:
        y=random.randrange(6)
        x.sleep(y)
        f1=opp(z,b1)
        print("%s\'s card:"%b,f1)
        if f1 not in ["colour","+4","take"]:
            if(f1 in b1):
                g1=z.split()
                for i in g1:
                    if(i in f1):
                        z=f1
                        e.append(f1)
                        b1.remove(f1)
                        if("+2" in f1):
                            if (j==0):
                                for i in range(2):
                                    d3=random.choice(e)
                                    c1.append(d3)
                                    e.remove(d3)
                                print("%s taken two cards"%c)
                            else:
                                for i in range(2):
                                    d3=random.choice(e)
                                    a1.append(d3)
                                    e.remove(d3)
                                print("%s taken two cards"%a)
                            if(j==0):
                                h=3
                            else:
                                h=1
                            break
                        elif("turn" in f1):
                            if(j==0):
                                j=1
                                print("%s turned the game"%b)
                            else:
                                j=0
                                print("%s turned the game"%b)
                            break
                        elif("skip" in f1):
                            if(j==0):
                                h=3
                                print("%s\'s chance skipped"%c)
                            else:
                                h=1
                                print("%s\'s chance skipped"%a)
                            break
                        else:
                            break
        elif("colour" in f1):
            k=colour(b1)
            print("%s selected %s colour"%(b,k))
            if(k=="red"):
                z="red"
            elif(k=="blue"):
                z="blue"
            elif(k=="green"):
                z="green"
            elif(k=="yellow"):
                z="yellow"
            e.append(f1)
            b1.remove(f1)
        elif("+4" in f1):
            k=colour(b1)
            print("%s selected %s colour"%(b,k))            
            if(k=="red"):
                z="red"
            elif(k=="blue"):
                z="blue"
            elif(k=="green"):
                z="green"
            elif(k=="yellow"):
                z="yellow"
            if (j==0):
                for i in range(4):
                    d3=random.choice(e)
                    c1.append(d3)
                    e.remove(d3)
                print("%s taken four cards"%c)
            else:
                for i in range(4):
                    d3=random.choice(e)
                    a1.append(d3)
                    e.remove(d3)
                print("%s taken four cards"%a)
            if(j==0):
                h=3
            else:
                h=1
            e.append(f1)
            b1.remove(f1)
        else:
            print("%s taken a card"%b)
            d4=random.choice(e)
            b1.append(d4)
            e.remove(d4)
            f1=d4
            if f1 not in ["colour","+4"]:
                if(f1 in b1):
                    g1=z.split()
                    for i in g1:
                        if(i in f1):
                            print("%s kept the taken card:"%b,f1)
                            z=f1
                            e.append(f1)
                            b1.remove(f1)
                            if("+2" in f1):
                                if (j==0):
                                    for i in range(2):
                                        d3=random.choice(e)
                                        c1.append(d3)
                                        e.remove(d3)
                                    print("%s taken two cards"%c)
                                else:
                                    for i in range(2):
                                        d3=random.choice(e)
                                        a1.append(d3)
                                        e.remove(d3)
                                    print("%s taken two cards"%a)
                                if(j==0):
                                    h=3
                                else:
                                    h=1
                                break
                            elif("turn" in f1):
                                if(j==0):
                                    j=1
                                    print("%s turned the game"%b)
                                else:
                                    j=0
                                    print("%s turned the game"%b)
                                break
                            elif("skip" in f1):
                                if(j==0):
                                    h=2
                                    print("%s\'s chance skipped"%c)
                                else:
                                    h=4
                                    print("%s\'s chance skipped"%a)
                                break
                            else:
                                break
            elif("colour" in f1):
                print("%s kept the taken card:"%b,f1)
                k=colour(b1)
                print("%s selected %s colour"%(b,k))
                if(k=="red"):
                    z="red"
                elif(k=="blue"):
                    z="blue"
                elif(k=="green"):
                    z="green"
                elif(k=="yellow"):
                    z="yellow"
                e.append(f1)
                b1.remove(f1)
            elif("+4" in f1):
                print("%s kept the taken card:"%b,f1)
                k=colour(b1)
                print("%s selected %s colour"%(b,k))
                if(k=="red"):
                    z="red"
                elif(k=="blue"):
                    z="blue"
                elif(k=="green"):
                    z="green"
                elif(k=="yellow"):
                    z="yellow"
                if (j==0):
                    for i in range(4):
                        d3=random.choice(e)
                        c1.append(d3)
                        e.remove(d3)
                    print("%s taken four cards"%c)
                else:
                    for i in range(4):
                        d3=random.choice(e)
                        a1.append(d3)
                        e.remove(d3)
                    print("%s taken four cards"%a)
                if(j==0):
                    h=3
                else:
                    h=1
                e.append(f1)
                b1.remove(f1)
        l=len(b1)
        if(l==1):
            print("%s said UNO"%b)
        elif(l==0):
            break
    elif h==3:
        y=random.randrange(6)
        x.sleep(y)
        f1=opp(z,c1)
        print("%s\'s card:"%c,f1)
        if f1 not in ["colour","+4","take"]:
            if(f1 in c1):
                g1=z.split()
                for i in g1:
                    if(i in f1):
                        z=f1
                        e.append(f1)
                        c1.remove(f1)
                        if("+2" in f1):
                            if (j==0):
                                for i in range(2):
                                    d3=random.choice(e)
                                    d1.append(d3)
                                    e.remove(d3)
                                print("%s taken two cards"%d)
                            else:
                                for i in range(2):
                                    d3=random.choice(e)
                                    b1.append(d3)
                                    e.remove(d3)
                                print("%s taken two cards"%b)
                            if(j==0):
                                h=4
                            else:
                                h=2
                            break
                        elif("turn" in f1):
                            if(j==0):
                                j=1
                                print("%s turned the game"%c)
                            else:
                                j=0
                                print("%s turned the game"%c)
                            break
                        elif("skip" in f1):
                            if(j==0):
                                h=4
                                print("%s\'s chance skipped"%d)
                            else:
                                h=2
                                print("%s\'s chance skipped"%b)
                            break
                        else:
                            break
        elif("colour" in f1):
            k=colour(c1)
            print("%s selected %s colour"%(c,k))
            if(k=="red"):
                z="red"
            elif(k=="blue"):
                z="blue"
            elif(k=="green"):
                z="green"
            elif(k=="yellow"):
                z="yellow"
            e.append(f1)
            c1.remove(f1)
        elif("+4" in f1):
            k=colour(c1)
            print("%s selected %s colour"%(c,k))
            if(k=="red"):
                z="red"
            elif(k=="blue"):
                z="blue"
            elif(k=="green"):
                z="green"
            elif(k=="yellow"):
                z="yellow"
            if (j==0):
                for i in range(4):
                    d3=random.choice(e)
                    d1.append(d3)
                    e.remove(d3)
                print("%s taken four cards"%d)
            else:
                for i in range(4):
                    d3=random.choice(e)
                    b1.append(d3)
                    e.remove(d3)
                print("%s taken four cards"%b)
            if(j==0):
                h=4
            else:
                h=2
            e.append(f1)
            c1.remove(f1)
        else:
            print("%s taken a card"%c)
            d4=random.choice(e)
            c1.append(d4)
            e.remove(d4)
            f1=d4
            if f1 not in ["colour","+4"]:
                if(f1 in b1):
                    g1=z.split()
                    for i in g1:
                        if(i in f1):
                            print("%s kept the taken card:"%c,f1)
                            z=f1
                            e.append(f1)
                            c1.remove(f1)
                            if("+2" in f1):
                                if (j==0):
                                    for i in range(2):
                                        d3=random.choice(e)
                                        d1.append(d3)
                                        e.remove(d3)
                                    print("%s taken two cards"%d)
                                else:
                                    for i in range(2):
                                        d3=random.choice(e)
                                        b1.append(d3)
                                        e.remove(d3)
                                    print("%s taken two cards"%b)
                                if(j==0):
                                    h=4
                                else:
                                    h=2
                                break
                            elif("turn" in f1):
                                if(j==0):
                                    j=1
                                    print("%s turned the game"%c)
                                else:
                                    j=0
                                    print("%s turned the game"%c)
                                break
                            elif("skip" in f1):
                                if(j==0):
                                    h=4
                                    print("%s\'s chance skipped"%d)
                                else:
                                    h=2
                                    print("%s\'s chance skipped"%b)
                                break
                            else:
                                break
            elif("colour" in f1):
                print("%s kept the taken card:"%c,f1)
                k=colour(c1)
                print("%s selected %s colour"%(c,k))
                if(k=="red"):
                    z="red"
                elif(k=="blue"):
                    z="blue"
                elif(k=="green"):
                    z="green"
                elif(k=="yellow"):
                    z="yellow"
                e.append(f1)
                c1.remove(f1)
            elif("+4" in f1):
                print("%s kept the taken card:"%c,f1)
                k=colour(c1)
                print("%s selected %s colour"%(c,k))
                if(k=="red"):
                    z="red"
                elif(k=="blue"):
                    z="blue"
                elif(k=="green"):
                    z="green"
                elif(k=="yellow"):
                    z="yellow"
                if (j==0):
                    for i in range(4):
                        d3=random.choice(e)
                        d1.append(d3)
                        e.remove(d3)
                    print("%s taken four cards"%d)
                else:
                    for i in range(4):
                        d3=random.choice(e)
                        b1.append(d3)
                        e.remove(d3)
                    print("%s taken four cards"%b)
                if(j==0):
                    h=4
                else:
                    h=2
                e.append(f1)
                c1.remove(f1)
        l=len(c1)
        if(l==1):
            print("%s said UNO"%c)
        elif(l==0):
            break
    elif h==4:
        y=random.randrange(6)
        x.sleep(y)
        f1=opp(z,d1)
        print("%s\'s card:"%d,f1)
        if f1 not in ["colour","+4","take"]:
            if(f1 in d1):
                g1=z.split()
                for i in g1:
                    if(i in f1):
                        z=f1
                        e.append(f1)
                        d1.remove(f1)
                        if("+2" in f1):
                            if (j==0):
                                for i in range(2):
                                    d3=random.choice(e)
                                    a1.append(d3)
                                    e.remove(d3)
                                print("%s taken two cards"%a)
                            else:
                                for i in range(2):
                                    d3=random.choice(e)
                                    c1.append(d3)
                                    e.remove(d3)
                                print("%s taken two cards"%c)
                            if(j==0):
                                h=1
                            else:
                                h=3
                            break
                        elif("turn" in f1):
                            if(j==0):
                                j=1
                                print("%s turned the game"%d)
                            else:
                                j=0
                                print("%s turned the game"%d)
                            break
                        elif("skip" in f1):
                            if(j==0):
                                h=1
                                print("%s\'s chance skipped"%a)
                            else:
                                h=3
                                print("%s\'s chance skipped"%c)
                            break
                        else:
                            break
        elif("colour" in f1):
            k=colour(d1)
            print("%s selected %s colour"%(d,k))
            if(k=="red"):
                z="red"
            elif(k=="blue"):
                z="blue"
            elif(k=="green"):
                z="green"
            elif(k=="yellow"):
                z="yellow"
            e.append(f1)
            d1.remove(f1)
        elif("+4" in f1):
            k=colour(d1)
            print("%s selected %s colour"%(d,k))
            if(k=="red"):
                z="red"
            elif(k=="blue"):
                z="blue"
            elif(k=="green"):
                z="green"
            elif(k=="yellow"):
                z="yellow"
            if (j==0):
                for i in range(4):
                    d3=random.choice(e)
                    a1.append(d3)
                    e.remove(d3)
                print("%s taken four cards"%a)
            else:
                for i in range(4):
                    d3=random.choice(e)
                    c1.append(d3)
                    e.remove(d3)
                print("%s taken four cards"%c)
            if(j==0):
                h=1
            else:
                h=3
            e.append(f1)
            d1.remove(f1)
        else:
            print("%s taken a card"%d)
            d4=random.choice(e)
            d1.append(d4)
            e.remove(d4)
            f1=d4
            if f1 not in ["colour","+4"]:
                if(f1 in b1):
                    g1=z.split()
                    for i in g1:
                        if(i in f1):
                            print("%s kept the taken card:"%d,f1)
                            z=f1
                            e.append(f1)
                            d1.remove(f1)
                            if("+2" in f1):
                                if (j==0):
                                    for i in range(2):
                                        d3=random.choice(e)
                                        a1.append(d3)
                                        e.remove(d3)
                                    print("%s taken two cards"%a)
                                else:
                                    for i in range(2):
                                        d3=random.choice(e)
                                        c1.append(d3)
                                        e.remove(d3)
                                    print("%s taken two cards"%c)
                                if(j==0):
                                    h=1
                                else:
                                    h=3
                                break
                            elif("turn" in f1):
                                if(j==0):
                                    j=1
                                    print("%s turned the game"%d)
                                else:
                                    j=0
                                    print("%s turned the game"%d)
                                break
                            elif("skip" in f1):
                                if(j==0):
                                    h=1
                                    print("%s\'s chance skipped"%a)
                                else:
                                    h=3
                                    print("%s\'s chance skipped"%c)
                                break
                            else:
                                break
            elif("colour" in f1):
                print("%s kept the taken card:"%d,f1)
                k=colour(d1)
                print("%s selected %s colour"%(d,k))
                if(k=="red"):
                    z="red"
                elif(k=="blue"):
                    z="blue"
                elif(k=="green"):
                    z="green"
                elif(k=="yellow"):
                    z="yellow"
                e.append(f1)
                d1.remove(f1)
            elif("+4" in f1):
                print("%s kept the taken card:"%d,f1)
                k=colour(c1)
                print("%s selected %s colour"%(d,k))
                if(k=="red"):
                    z="red"
                elif(k=="blue"):
                    z="blue"
                elif(k=="green"):
                    z="green"
                elif(k=="yellow"):
                    z="yellow"
                if (j==0):
                    for i in range(4):
                        d3=random.choice(e)
                        a1.append(d3)
                        e.remove(d3)
                    print("%s taken four cards"%a)
                else:
                    for i in range(4):
                        d3=random.choice(e)
                        c1.append(d3)
                        e.remove(d3)
                    print("%s taken four cards"%c)
                e.append(f1)
                d1.remove(f1)
                if(j==0):
                    h=1
                else:
                    h=3
        l=len(d1)
        if(l==1):
            print("%s said UNO"%d)
        elif(l==0):
            break
    if(j==0):
        if(h==4):
            h=1
        else:
            h=h+1
    else:
        if(h==1):
            h=4
        else:
            h=h-1
if(h==1):
    print(format("%s won the match"%a,"^70"))
elif(h==2):
    print(format("%s won the match"%b,"^70"))
elif(h==3):
    print(format("%s won the match"%c,"^70"))
if(h==4):
    print(format("%s won the match"%d,"^70"))


            
            

                                
                                
                            
                
                
                
    




import random
egyenleg=10000
while True:
    print(egyenleg)
    tét=int(input("Add meg a téted."))
    while tét>egyenleg:
        print("Töbet raktálbe mint az egyenleged.")
        tét=int(input("Add meg a téted."))   
    if tét==0:
        break
    szín=int(input("1:fekete 2:piros")) 
    sorsolt=random.randint(0,36)
    if sorsolt % 2 ==0:
        print("fekete") 
        if szín==1:
            egyenleg+=tét
        else : egyenleg-=tét
    else :
        print("piros")
        if szín==2:
            egyenleg+=tét
        else : egyenleg-=tét
    if egyenleg<=0:
        print("elfogyott a pénzed")
        break

 

##Dict1={"G":"glycine","T":"threonine","A":"alanine"}
##print(Dict1["T"])
##print("T" in Dict1)
##print("t" in Dict1)
##print(Dict1.values())
##print(Dict1.keys())

##names=["H","He","Li","Be"]
##masses=[1.008,4.003,6.941,9.012]
##Dict2={}
##for i in range(len(names)):
##    Dict2[names[i]]=masses[i]
##print(Dict2)
##print(Dict2["He"])
##print("O" in Dict2)

##names=["H","He","Li","Be"]
##masses=[1.008,4.003,6.941,9.012]
##Dict3=dict(zip(names,masses))
##print(Dict3)
##print(Dict3["He"])
##print("O" in Dict3)    

import math
funcs={"sqrt":math.sqrt,"ln":math.log,"log":math.log10}
f="start"
while f!="stop":
    n=int(input("Enter number:"))
    f=input("Function to perform (or stop):")
    if not f in funcs:
        print("No such function")
    else:
        print("Applying function %s to %d yields %f"%(f,n,funcs[f](n)))

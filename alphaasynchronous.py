import math
import random
def binary(rule):
    m=""
    while(rule!=0):
        d=rule%2
        if d==0:
            m+='0'
        else:
            m+='1'
        rule//=2
    while(len(m)!=8):
        m+='0'
    m=m[::-1]
    return m

rule=int(input("Enter the rule :"))
n=int(input("Enter the lattice size :"))
rulebin=binary(rule)
Rule={
    '111':rulebin[0],
    '110':rulebin[1],
    '101':rulebin[2],
    '100':rulebin[3],
    '011':rulebin[4],
    '010':rulebin[5],
    '001':rulebin[6],
    '000':rulebin[7],
}
print("Rule is :")
print("Pattern        Next State for center cell")
for i in Rule:
    print(" ",i,"                 ",Rule[i])
states=[]
alpha=float(input("Enter alpha :"))
num=math.ceil(alpha*n)
print("Number of randomly choosed cells that will be updated is ",num)
c=input("Enter Initial Configuration :")
time=int(input("Enter the number of time steps :"))
count=1
while count<=time:
    rand=random.sample(range(1,n+1),num)
    rand.sort()
    states.append(c)
    next=""
    new=c[len(c)-1]+c
    new+=new[1]
    for i in range(len(c)):
        if i+1 in rand:
            next+=Rule[str(new[i:i+3])]
        else:
            next+=new[i+1]
    print("Next configuration :",next," The position of cells that were selected and updated :",rand)
    c=next
    count+=1
print("The Transition Diagram is :")
for i in states:
    print(i," -> ",end="")
print(c)
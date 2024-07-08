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
#print(rulebin)
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
c=input("Enter Initial Configuration :")
while c not in states:
    states.append(c)
    next=""
    new=c[len(c)-1]+c
    new+=new[1]
    #print(new)
    for i in range(len(c)):
        next+=Rule[str(new[i:i+3])]
    #print(next)
    c=next
print("The Transition Diagram is :")
for i in states:
    print(i," -> ",end="")
print(c)
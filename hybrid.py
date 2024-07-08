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
def binaryadd(a,b):
    sum = bin(int(a, 2) + int(b, 2))
    l=str(sum[2:])
    while len(l)!=n:
        l="0"+l
    return l
n=int(input("Enter the lattice size :"))
rulevector=eval(input("Enter the rule vector:"))
c="0"*n
one="0"*(n-1)+"1"
m=c
displayed=[]
covered=[]
waste=0
while m.count("1")<=n:
    if m not in covered:
        c=m
        states=[]
        while c not in states:
            states.append(c)
            next=""
            new="0"+c
            new+="0"
            for i in range(len(c)):
                rule=rulevector[i]
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
                if rulevector[i] not in displayed:
                    print("Rule",rulevector[i]," is :")
                    print("Pattern        Next State for center cell")
                    for j in Rule:
                        print(" ",j,"                 ",Rule[j])
                displayed.append(rulevector[i])
                next+=Rule[str(new[i:i+3])]
            covered.append(c)
            c=next
        if waste==0:
            print("The Transition Diagram is :")
        waste+=1
        for i in states:
            print(i," -> ",end="")
        print(c)
    if(m.count("1")==n):
        exit(0)
    m=binaryadd(m,one)
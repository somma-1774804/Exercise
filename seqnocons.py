def nocons(S):
    l = len(S)
    T = [0] * l
    for i in range(0, l):
        if i==l-1 : T[i]=T[i-1]
        else :
            m = max(S[i], S[i+1])
            if i>0 and T[i-1]==S[i-1] or T[i-1]==S[i+1] :
                T[i]= max(T[i],T[i-1])
                T[i-1]= max(T[i],T[i-1])
            else : T[i]=m
    sum = 0
    sub = []
    for i in T:
        if i not in sub:
            sub.append(i)
            sum = sum + i
    print(sub)
    return sum

S=[1,5,4,6,10,3,2,9]
print(nocons(S))

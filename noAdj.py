def noAdjBk(n):
    set ={0,1,2}
    for x in set :
        noAdjP(n,[x],1)
def noAdjP(n,sol,i):
    if i==n :
        print(sol)
    else:
        if sol[-1]%2==0:
            sol.append(1)
            noAdjP(n,sol,i+1)
            sol.pop()
        else:
            sol.append(0)
            noAdjP(n, sol, i + 1)
            sol.pop()
            sol.append(2)
            noAdjP(n, sol, i + 1)
            sol.pop()

noAdjBk(3)

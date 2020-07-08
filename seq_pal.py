def seq_pal_c(n):
    return seq_pal(2,[],0,2*(n)-1)
def seq_pal(n,sol,i,j):
    if i == (2*n) :
        print(''.join(sol))
    else :
        if i<=n-1 or sol[j]=='a':
            sol.append('a')
            seq_pal(n,sol,i+1,j-1)
            sol.pop()
        if i<=n-1 or sol[j]=='b':
            sol.append('b')
            seq_pal(n,sol,i+1,j-1)
            sol.pop()

seq_pal_c(2)


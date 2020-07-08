# Dato un intero n, stampa tutte le stringhe palindromi lunghe 2n con valori
# {a,b}. L'algoritmo deve avere complessita' O(n2^n)

def seq_pal_c(n):
    return seq_pal(2,[],0,2*(n)-1)

# Usando i due indici i e j , rispettivamente inizializzati a 0 e 2n-1, incremento i e decremento j fino a ad arrivare ad n.
# A questo punto j mi dirà cosa posso o non posso mettere nella seconda metà della sequenza scorrendo la metà sequenza da n a 0.

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


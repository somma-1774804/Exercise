def formatta_matrice(matrice):
    return '\n'.join([''.join(['{:2}'.format(x) for x in i]) for i in matrice])

def matr_crescente(n):
    def matr_crescente_bt(n, i, j, sol):
        set = {1, 2, 3}
        def matr_cresc2(n, i, j, sol,c):
           sol[i][j]=c
           if j < n - 1:
               matr_crescente_bt(n, i, j + 1, sol)
           else:
               matr_crescente_bt(n, i + 1, 0, sol)

        if i==n:
           print(formatta_matrice(sol))
           print()
        else :
            for y in set:
                if i==0 and j==0: matr_cresc2(n,i,j,sol,y)
                vicini_ok=True
                if i==0 and j>0:
                    vicini_ok &= sol[i][j-1]<=y
                if i>0 and j>0:
                    vicini_ok &= sol[i-1][j]<=y and sol[i][j-1]<=y
                if i>0 and j==0:
                    vicini_ok &= sol[i-1][j]<=y and sol[i][j+1]>=y

            if vicini_ok : matr_cresc2(n,i,j,sol,y)



    sol = [[0 for j in range(n)] for i in range(n)]
    matr_crescente_bt(2,0,0,sol)

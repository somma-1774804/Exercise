#Progettare un algoritmo che prende come parametro
# l’intero n e, in tempo O(n), restituisce il numero delle sequenze cui siamo interessati.
# Ad esempio:
# • per n = 1 la risposta dell’algoritmo deve essere 10
# • per n = 2 la risposta dell’algoritmo deve essere 75

def pariNotadj(n):
    from math import ceil
    T=[0 for _ in range(n+1)]
    T[0]=0
    T[1]=10

    print('prova:', T[1]/2)

    for i in range(2,n+1):
        T[i]= ceil(T[i-1]/2)*9+(ceil(T[i-1]/2)*5)+1
    return T[n]+4

print(pariNotadj(2))

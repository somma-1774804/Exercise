# Algoritmo che dato l’intero n, stampa tutte le sequenze lunghe n formate da interi nell’insieme {1, 2, 3, 4}
# con la proprietà che nella sequenza numeri adiacenti distano almeno 2.

def seq_ad_2(n):
    set= {1,2,3,4}
    for x in set :
       seq_ad_2bis(n,[x],set,1)

# Per ogni elemento dell'insieme {1,2,3,4} chiamiamo la funzione seq_ad_2bis alla quale passo la lunghezza
# della sequanza che vogliamo generare, la sequenza con il primo elemento estratto dall'insieme e , l'insieme stesso
# e un indice per controllare la lunghezza della sequenza.
# L'algoritmo per ogni elemento dell'insieme controlla se rispetta la condizione e se la rispetta
# l'elemento viene aggiunto alla sequenza fino a raggiungere la sequenza imposta (n).
def seq_ad_2bis(n,sol,set,i):
    if i==n:
        print(sol)
        return
    for y in set :
        if y >= sol[-1]+2 or  y <= sol[-1]-2:
            sol.append(y)
            seq_ad_2bis(n,sol,set,i+1)
            sol.pop()

seq_ad_2(3)



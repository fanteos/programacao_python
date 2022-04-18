#Escreva um programa em python com uma função que receba uma lista 
#L ordenada de números inteiros. A função deve retornar a mediana de L.

#Para a seguinte entrada:
#[1, 3, 7, 12, 15, 17, 19]

#A função deverá retornar:
#12

# =============================================================================
# Nossa Função
# =============================================================================
def calcular_mediana(lista):
    mediana = 0
    
    if((len(lista) % 2) == 0):
        mediana = lista[int(len(lista) / 2)]
        mediana += lista[int(len(lista) / 2) -1]
        mediana = mediana / 2
    else:
        mediana = lista[int(len(lista) / 2)]
        
    return mediana

# =============================================================================
# Nosso Código
# =============================================================================
l1 = [1, 3, 7, 12, 15, 17, 19]
print("%f" % calcular_mediana(l1))

l2 = [1, 3, 7, 12, 13, 15, 17, 19]
print("%f" % calcular_mediana(l2))
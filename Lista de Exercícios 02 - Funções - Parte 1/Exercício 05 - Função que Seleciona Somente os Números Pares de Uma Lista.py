#Escreva um programa em python com uma função que receba uma lista B
#de números inteiros. A função então deverá retornar uma nova lista 
#somente com os números pares de B.

#Para a seguinte entrada: 
    #[2, 5, 6, 3, 8, 3, 6, 3, 4, 5, 1]

#A função deverá retornar: 
    #[2, 6, 8, 6, 4]

# =============================================================================
# Funções
# =============================================================================
def separar_pares(lista):
    lista_pares = list([])
    for i in range(len(lista)):
        if((lista[i] % 2) == 0):
            lista_pares.append(lista[i])
    
    return lista_pares


# =============================================================================
# Main
# =============================================================================
lista_teste = [2, 5, 6, 3, 8, 3, 6, 3, 4, 5, 1]
lista_pares = separar_pares(lista_teste)
print(lista_pares)




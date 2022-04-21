#Escreva um programa em python com uma função que receba uma lista A
#de números inteiros. A função então deverá retornar uma nova lista 
#contendo somente uma ocorrência de cada elemento de A.

#Para a seguinte entrada: [2, 5, 6, 3, 8, 3, 6, 3, 4, 5, 1]

#A função deverá retornar: [2, 5, 6, 3, 8, 4, 5, 1]

# =============================================================================
# Funções
# =============================================================================
def elementos_unicos(lista):
    #forma 1
    #lista_unicos = set(lista)
    #lista_unicos = list(lista_unicos)
    
    #forma 2
    lista_unicos = list([])
    for elemento_atual in lista:
        if(not elemento_atual in lista_unicos):
            lista_unicos.append(elemento_atual)
    
    return lista_unicos



# =============================================================================
# Main
# =============================================================================
lista_inicial = [2, 5, 6, 3, 8, 3, 6, 3, 4, 5, 1]
lista_unicos = elementos_unicos(lista_inicial)
print(lista_unicos)



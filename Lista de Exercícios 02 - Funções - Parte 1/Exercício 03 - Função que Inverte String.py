#Escreva um programa em python com uma função que receba uma cadeia de 
#caracteres (string) e retorne essa string invertida.

#Para a seguinte entrada:
#Input String

#A função deverá retornar:
#gnirtS tupnI

# =============================================================================
# Funções
# =============================================================================
def invertir_string(string):
    #forma 1
    #string_invertida = string[::-1]
    
    #forma 2
    #string_invertida = list(string)
    #string_invertida.reverse()
    #string_invertida = str().join(string_invertida)
    
    #forma 3
    string_invertida = ""
    for i in range(len(string)):
        string_invertida = string_invertida + string[len(string) -i -1]
    
    return string_invertida



# =============================================================================
# Main
# =============================================================================
teste = "Input String"
print("%s" % invertir_string(teste))

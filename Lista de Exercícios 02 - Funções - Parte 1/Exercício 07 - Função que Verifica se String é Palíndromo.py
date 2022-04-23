#Escreva um programa em python com uma função que receba 
#uma cadeia de caracteres (string) e verifique se a string
#é um palíndromo. 
#Um palíndromo é uma sequência de caracteres ou números 
#que pode ser lida em sentido normal ou sentido 
#invertido e terá o mesmo significado. 
#Exemplos de palíndromos são: ana, otto e ovo.  
#A função deverá retornar um booleano com valor True se a string
#for um palíndromo ou False caso contrário. 

#Para a seguinte entrada: 
    #arara

#A função deverá retornar: 
    #True

# =============================================================================
# Função
# =============================================================================
def verificar_palindromo(string):
    flag = False
    
    string_invertida = string[::-1]
    
    if(string == string_invertida):
        flag = True
    
    return flag



# =============================================================================
# Main
# =============================================================================
teste1 = "arara"
print(verificar_palindromo(teste1))

teste2 = "3arara3"
print(verificar_palindromo(teste2))

teste3 = "ararra"
print(verificar_palindromo(teste3))
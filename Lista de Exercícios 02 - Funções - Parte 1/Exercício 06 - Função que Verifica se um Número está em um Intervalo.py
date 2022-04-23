#Escreva um programa em python com uma função que receba um numero 
#inteiro e verifique se o número está no intervalo [0, 55]. 
#A função deverá retornar um booleano com True se o número estiver 
#no intervalo ou False caso contrário. 

#Para a seguinte entrada: 
    #7

#A função deverá retornar: 
    #True

# =============================================================================
# Função
# =============================================================================
def verificar_intervalo(numero, intervalo = [0, 55]):
    flag = False
    
    if((numero >= intervalo[0]) and (numero <= intervalo[1])):
        flag = True
        
    return flag



# =============================================================================
# Main
# =============================================================================
print(verificar_intervalo(7))

print(verificar_intervalo(7, [0, 6]))

print(verificar_intervalo(55))

#Escreva um programa utilizando a linguagem python com uma função que receba 
#qualquer quantidade de números inteiros do usuário. A função parará de receber
# números quando o número zero for inserido. A função deverá retornar os
# números recebidos como uma lista.


# =============================================================================
# Nossa função
# =============================================================================
def receber_entrada():
    nossa_lista = []
    
    while(True):
        nosso_numero = int(input("Por favor insira um número (0 para sair): "))

        if(nosso_numero == 0):
            return nossa_lista
        
        nossa_lista.append(nosso_numero)




# =============================================================================
# O resto do programa
# =============================================================================

l = receber_entrada()
print(l)
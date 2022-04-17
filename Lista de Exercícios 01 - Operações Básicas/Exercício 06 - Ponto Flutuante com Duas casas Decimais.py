#Escreva um programa que receba um número ponto flutuante do usuário e exiba
# o número informado com duas casas decimais.

#Para a seguinte entrada:
    #3.141592
#A saída deverá ser: 
    #3.14

#Para a seguinte entrada:
    #13
#A saída deverá ser: 
    #13.00
    

#Receber o Número
nosso_numero = float(input("Por favor insira o número: "))

#Imprimir o Resultado
print("%.2f" % nosso_numero)
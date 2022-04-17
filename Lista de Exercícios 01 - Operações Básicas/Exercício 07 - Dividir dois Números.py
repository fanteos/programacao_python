#Escreva um programa que receba dois números do usuário e exiba na 
#tela o resultado do primeiro divido pelo segundo.


#Para a seguinte entrada: 
    #3
    #4
#A saída deverá ser:
    #0.75
    

#Receber os números
numero_1 = int(input("Por favor insira o primeiro número: "))
numero_2 = int(input("Por favor insira o segundo número: "))

#imprimir o resultado
print("%.2f" % (numero_1 / numero_2))
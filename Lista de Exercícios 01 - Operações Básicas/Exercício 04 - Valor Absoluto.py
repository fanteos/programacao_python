#Escreva um programa que receba dois números do usuário e exiba na tela o valor 
#absoluto da diferença do primeiro menos o segundo número

#Para a seguinte entrada:
#4
#12

#A saída deverá ser:
#A diferença absoluta de 4 e 12 é 8.


#Receber os dois números
primeiro_numero = int(input("Por favor insira o primeiro número: "))
segundo_numero = int(input("Por favor insira o segundo número: "))

#Computar o valor absoluto da diferença
resultado = abs(primeiro_numero - segundo_numero)


#Exibir o resultado
print("A diferença absoluta de %d e %d é %d." % (primeiro_numero, segundo_numero, resultado))
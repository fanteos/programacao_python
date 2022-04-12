#Escreva um script que receba três números inteiros e exiba o mínimo e o máximo



#receber três números inteiros
primeiro_numero = int(input("Por favor insira o primeiro número: "))
segundo_numero = int(input("Por favor insira o segundo número: "))
terceiro_numero = int(input("Por favor insira o terceiro número: "))


#computar qual o mínimo e máximo
#nosso_maximo = max(primeiro_numero, segundo_numero, terceiro_numero)

nosso_maximo = primeiro_numero
if(segundo_numero > nosso_maximo):
    nosso_maximo = segundo_numero
if(terceiro_numero > nosso_maximo):
    nosso_maximo = terceiro_numero


#nosso_minimo = min(primeiro_numero, segundo_numero, terceiro_numero)

nosso_minimo = primeiro_numero
if(segundo_numero < nosso_minimo):
    nosso_minimo = segundo_numero
if(terceiro_numero < nosso_minimo):
    nosso_minimo = terceiro_numero
    
    
    
#exibir o mínimo e o máximo
print("O mínimo é %d." % nosso_minimo)
#print("O mínimo é ", nosso_minimo, ".", sep="")

print("O máximo é %d." % nosso_maximo)
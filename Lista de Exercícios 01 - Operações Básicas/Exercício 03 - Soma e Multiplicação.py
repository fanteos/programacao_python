#Escreva um script que receba dois números inteiros e exiba a soma e a multiplicação dos números


#receber os números
primeiro_numero = int(input("Por favor insira o primeiro número: "))
segundo_numero = int(input("Por favor insira o segundo número: "))

#computar a soma e multiplicação
#nossa_soma = sum(primeiro_numero, segundo_numero)

nossa_soma = primeiro_numero + segundo_numero

nossa_mult = primeiro_numero * segundo_numero


#exibir os resultados
print("A soma de %d e %d é: %d." % (primeiro_numero, segundo_numero, nossa_soma))
#print("A soma de ", primeiro_numero," e ", segundo_numero, " é: ", nossa_soma, ".", sep="")

print("A multiplicação de %d e %d é: %d." % (primeiro_numero, segundo_numero, nossa_mult))
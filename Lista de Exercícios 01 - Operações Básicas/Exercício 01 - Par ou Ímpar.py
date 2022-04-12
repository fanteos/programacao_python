#Receba um número inteiro do usuário e exiba se o número é ímpar ou par


#receber o número inteiro
nosso_numero = int(input("Por favor insira um número inteiro: "))


#verificar se é impar ou par e exibir o resultado
if((nosso_numero % 2) == 0):
    print("O número informado (%d) é par" % nosso_numero)
else:
    print("O número informado (%d) é impar." % nosso_numero)
        
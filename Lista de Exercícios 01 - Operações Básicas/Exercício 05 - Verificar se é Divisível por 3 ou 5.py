#Escreva um script que receba um número inteiro do usuário e exiba na tela 
#se o número é divisível por 3 ou 5.

#Para a seguinte entrada:
#15
#A saída deverá ser: 
#O número 15 é divisível por 3 e 5.

#Para a seguinte entrada: 
#9
#A saída deverá ser: 
#O número 9 é divisível por 3.

#Para a seguinte entrada: 
#2

#A saída deverá ser: 
#O número 2 não é divisível por 3 e nem por 5.


#Receber um número inteiro
nosso_numero = int(input("Por favor insira um número: "))

#Verificar se é divisível
eh_divisivel_por_3 = False
if((nosso_numero % 3) == 0):
    eh_divisivel_por_3 = True

eh_divisivel_por_5 = False
if((nosso_numero % 5) == 0):
    eh_divisivel_por_5 = True
    
    
#Exibir os resultados
if(eh_divisivel_por_3 & eh_divisivel_por_5):
    print("O número %d é divisível por 3 e 5." % nosso_numero)
elif(eh_divisivel_por_3):
    print("O número %d é divisível por 3." % nosso_numero)
elif(eh_divisivel_por_5):
    print("O número %d é divisível por 5." % nosso_numero)
else:
    print("O número %d não é divisível por 3 e nem por 5." % nosso_numero)







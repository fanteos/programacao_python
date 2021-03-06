# -*- coding: utf-8 -*-
"""L4 E4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E4WVrmBHXhdxc_RpFuyM_IYOmGYK52-I
"""

#Escreva um programa que possibilite ao usuário calcular a área e o 
#volume de diversas formas geométricas. Além disso, calcular o seno, cosseno 
#e tangente de um ângulo e calcular logaritmos de números. 
#O seu programa deve possuir o seguinte menu:

#a) 1 - Calcular a área de um quadrado
#b) 2 - Calcular a área de um círculo
#c) 3 - Calcular o volume de um paralelepípedo
#d) 4 - Calcular o volume de uma esfera
#e) 5 - Calcular o seno de um ângulo
#f) 6 - Calcular o cosseno de um ângulo
#g) 7 - Calcular a tangente de um ângulo
#h) 8 - Calcular o logaritmo de um número
#i) 9 - Sair do Programa

#Observação 1: Todos os valores informados e calculados no programa devem 
#ser pontos flutuantes.
#Observação 2: Considere π = 3, 14159265.
#Observação 3: Todos os valores exibidos pelas operações do programa devem 
#ser apresentados com oito casas decimais de precisão.
#Observação 4: Depois de executada qualquer operação, com exceção de 
#"Sair do Programa", o menu deve ser exibido novamente para o usuário.
#Observação 5: As opções 1, 2, 3 e 4 devem ser calculadas a partir 
#de funções implementadas por você.

#Bibliotecas
import math

#Valores Globais
PI_GLOBAL = 3.14159265

#Funções
def exibir_menu():
  print("\n1 - Calcular a área de um quadrado")
  print("2 - Calcular a área de um círculo")
  print("3 - Calcular o volume de um paralelepípedo")
  print("4 - Calcular o volume de uma esfera")
  print("5 - Calcular o seno de um ângulo")
  print("6 - Calcular o cosseno de um ângulo")
  print("7 - Calcular a tangente de um ângulo")
  print("8 - Calcular o logaritmo de um número")
  print("9 - Sair do Programa\n")

def area_quadrado(l):
  area = l**2
  return float(area)

def area_circulo(r):
  area = PI_GLOBAL * (r**2)
  return float(area)

def volume_paralelepipedo(l1, l2, l3):
  volume = l1 * l2 * l3
  return float(volume)

def volume_esfera(r):
  volume = (4/3) * PI_GLOBAL * (r**3)
  return float(volume)

#Main

exibir_menu()
opcao_usuario = int(input("Selecione uma opção: "))

while(opcao_usuario != 9):

  if(opcao_usuario == 1):
    lado = float(input("Insira o lado do quadrado: "))
    print("%.8f" % area_quadrado(lado))
  elif(opcao_usuario == 2):
    raio = float(input("Insira o raio do círculo: "))
    print("%.8f" % area_circulo(raio))
  elif(opcao_usuario == 3):
    lado1 = float(input("Insira o lado 1 do paralelepípedo: "))
    lado2 = float(input("Insira o lado 2 do paralelepípedo: "))
    lado3 = float(input("Insira o lado 3 do paralelepípedo: "))
    print("%.8f" % volume_paralelepipedo(lado1, lado2, lado3))
  elif(opcao_usuario == 4):
    raio = float(input("Insira o raio da esfera: "))
    print("%.8f" % volume_esfera(raio))
  elif(opcao_usuario == 5):
    a = float(input("Insira o ângulo desejado: "))
    print("%.8f" % math.sin(a))
  elif(opcao_usuario == 6):
    a = float(input("Insira o ângulo desejado: "))
    print("%.8f" % math.cos(a))
  elif(opcao_usuario == 7):
    a = float(input("Insira o ângulo desejado: "))
    print("%.8f" % math.tan(a))
  elif(opcao_usuario == 8):
    a = float(input("Insira o numero desejado: "))
    b = float(input("Insira a base desejada: "))
    print("%.8f" % math.log(a, b))

  exibir_menu()
  opcao_usuario = int(input("Selecione uma opção: "))
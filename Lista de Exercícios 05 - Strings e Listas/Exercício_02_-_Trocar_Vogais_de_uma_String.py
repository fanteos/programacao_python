# -*- coding: utf-8 -*-
"""L5 E2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M4RYlj0cKB9xhfz7D0r2pc3HDsyhjE3C
"""

#Escreva um programa que receba uma frase e troque todas as vogais 
#da frase pela letra A.

#Exemplo de entrada: Irei caminhar hoje
#Saída do programa: ArAA cAmAnhAr hAjA

#Funções
def trocar_caracteres(frase):
  frase = frase.replace("a", "A")
  frase = frase.replace("e", "A")
  frase = frase.replace("E", "A")
  frase = frase.replace("i", "A")
  frase = frase.replace("I", "A")
  frase = frase.replace("o", "A")
  frase = frase.replace("O", "A")
  frase = frase.replace("u", "A")
  frase = frase.replace("U", "A")
  return frase

#Main
frase_teste = "Irei caminhar hoje"
print(trocar_caracteres(frase_teste))

frase_teste2 = "Amanha eh segunda"
print(trocar_caracteres(frase_teste2))
# -*- coding: utf-8 -*-
"""L5 E6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oRUNLQtnZJrVTxu7SBkoHRRHQWnT4th7
"""

#Escreva um programa que receba separadamente o nome de uma pessoa 
#e os una em uma s? string.

#Para as entradas:
#"Felipe"
#"Antunes"
#"Dos Santos"
#A string final deve ser: "Felipe Antunes dos Santos"

#Main

nomes = []
p = input("Por favor insira um nome (0 para encerrar): ")

while(p != "0"):
  nomes.append(p)
  p = input("Por favor insira um nome (0 para encerrar): ")

nome_final = " ".join(nomes)
print(nome_final)
# -*- coding: utf-8 -*-
"""L6 E7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DWpv00ZJhj6WMeZsSo6zL3VI5qeUwnVv
"""

#Escreva um programa que copie o arquivo nomeado "Dia de sol na praia.png" 
#da pasta "Meus Arquivos" para a pasta "Viagem para a Praia". 
#Ambas as pastas "Meus Arquivos" e "Viagem para a Praia" devem estar no 
#mesmo diretório em que a resolução do exercício estiver.

#Bilbiotecas
import shutil, cv2
import matplotlib.pyplot as plt 

caminho_origem = "Meus Arquivos/Dia de sol na praia.png"
caminho_destino = "Viagem para a Praia/foto1.png"

shutil.copy(caminho_origem, caminho_destino)

#print("Imagem Origem")
#img_o = cv2.imread(caminho_origem)
#plt.imshow(img_o)

print("Imagem Destino")
img_d = cv2.imread(caminho_destino)
plt.imshow(img_d)
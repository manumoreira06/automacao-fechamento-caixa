import pdfplumber #biblioteca para ler pdf
import re #biblioteca para identificar padrões de texto
from collections import defaultdict #biblioteca para criar dicionarios com listas

#para ler uma pagina 
#with pdfplumber.open(r"C:\Users\sbkst\OneDrive\Documentos\Vendas por Espécie.pdf") as pdf:
'''primeira_pagina = pdf.pages[0]
    texto = primeira_pagina.extract_text()
    print(texto)'''
    

#para ler todas as paginas
with pdfplumber.open(r"C:\Vendas por Espécie.pdf") as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        #print(texto)
        #print(pdf.metadata)

linhas = texto.splitlines()
for linha in linhas:
    print(linha)

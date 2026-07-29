import pdfplumber

with pdfplumber.open("C:/Users/manuu/OneDrive/Documentos/Exercicios.pdf.pdf") as pdf:
    primeira_pagina = pdf.pages[0]
    texto = primeira_pagina.extract_text()
    print(texto)

linhas = texto.splitlines()
for linha in linhas:
    if linha.startswith("B:"):
        print(linha)


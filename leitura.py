import pdfplumber #biblioteca para ler pdf
import re #biblioteca para identificar padrões de texto
from collections import defaultdict #biblioteca para criar dicionarios com listas

venda = []
total = ""
venda_nota = {}


#para ler todas as paginas
with pdfplumber.open(r"C:\Vendas por Espécie.pdf") as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        #print(texto)
        linhas = texto.splitlines() #transforma o texto em linhas 

#PEGAR A FORMA DE PAGAMENTO 

        for linha in linhas:
             if linha.startswith("ESPÉCIE"):
                forma_pagamento = linha.replace("ESPÉCIE:", "").strip()
                if forma_pagamento == "CREDITO TEF":
                     forma_pagamento = "CC"
                if forma_pagamento == "DÉBITO TEF":
                     forma_pagamento = "CD"
                if forma_pagamento == "CREDITO":
                     forma_pagamento = "CC"
                if forma_pagamento == "CARTAO CREDITO":
                    forma_pagamento = "CC"
                if forma_pagamento == "CARTAO DEBITO":
                    forma_pagamento = "CD"
                if forma_pagamento == "DÉBITO":
                     forma_pagamento = "CD"
                if forma_pagamento == "PRAZO":
                     forma_pagamento = "ML"
                                     
             if linha.startswith("00"):
                    partes_venda = linha.split()
                    nota = partes_venda[0]
                    valor = partes_venda[-1]
                    valor = valor.replace(",", ".")
                    valor = float(valor)
    

        #JUNTAR TODAS AS INFORMAÇÕES EM UMA LISTA 
                    venda.append({
                         "nota": nota,
                         "pagamento": forma_pagamento,
                         "valor": valor
            })

                    if nota in venda_nota:
                        venda_nota[nota]["pagamento"].append(forma_pagamento)
                        venda_nota[nota]["valor"].append(valor)

                    else:
                        venda_nota[nota] = {}
                        venda_nota[nota]["pagamento"] = []
                        venda_nota[nota]["valor"] = []
                        venda_nota[nota]["pagamento"].append(forma_pagamento)
                        venda_nota[nota]["valor"].append(valor)

            #PEGAR O TOTAL DA VENDA
             if linha.startswith("*Os valores"):
                partes_total = linha.split()
                total = partes_total[-1]
            #dia da nota: 
             if linha.startswith("Período"):
                partes_periodo = linha.split()
                data = partes_periodo[2]

#rint(venda_nota)
#print(venda)

print(f"*VENDAS {data} R${total}")

for nota in venda_nota:
    valores = venda_nota[nota]["valor"]
    pagamentos = venda_nota[nota]["pagamento"]

    if len(valores) == 1:
        print(f"R${valores[0]} {pagamentos[0]}")
    else:
        soma = sum(valores)
        print(f"R${soma}(", end="") 
        for i in len([venda_nota[nota]["valor"]]):
            print(f"({valor[i]} {valor[i]})", end="")

#print("R$", valor, forma_pagamento,)
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
                if forma_pagamento == "DÉBITO":
                     forma_pagamento = "CD"

        #NUMERO DA NOTA - FORMA DE PAGAMENTO
            if linha.startswith("00"):
                    partes_venda = linha.split()
                    #print(partes_venda)
                    #print(partes_venda[0])
                    #print(partes_venda[0], "-", forma_pagamento) #tirar esse print pois é desnecessário para o final
                    #print(partes_venda[-1], "-", forma_pagamento) #Pega o ultimo item da lista (o valor)

        #JUNTAR TODAS AS INFORMAÇÕES EM UMA LISTA 
                    venda.append({
                "nota":partes_venda[0],
                "pagamento": forma_pagamento,
                "valor": partes_venda[-1]
            })

                if nota in venda_nota:
                    venda_nota[nota]["pagamento"].append(forma_pagamento)
                    venda_nota[nota]["valor"].append(partes_venda[-1])
                else:
                    venda_nota[nota] = {}
                    venda_nota[nota]["pagamento"] = []
                    venda_nota[nota]["valor"] = []
                    venda_nota[nota]["pagamento"].append(forma_pagamento)
                    venda_nota[nota]["valor"].append(partes_venda[-1])
                

            #PEGAR O TOTAL DA VENDA
            if linha.startswith("*Os valores"):
                partes_total = linha.split()
                total = partes_total[-1]
            #dia da nota: 
            if linha.startswith("Período"):
                partes_periodo = linha.split()
                data = partes_periodo[2]


#print(venda)
#print("TOTAL: R$", total)
#print("*VENDAS ",data "R$ ",total)
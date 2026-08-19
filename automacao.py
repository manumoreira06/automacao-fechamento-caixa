import pyautogui
import os 
import time


#abriri o sistema gdoor 
os.startfile(r"C:\GDOOR Sistemas\GDOOR PRO\GDOOR.exe")
time.sleep(25)
pyautogui.click(x=685, y=396)
pyautogui.write("123")
pyautogui.press("enter")
time.sleep(5)

#processo para aextrair o pdf

#abrindo o "vendas por especie"
pyautogui.click(x=524,y=490) #clicar em "relatorios"
time.sleep(3)
pyautogui.click(x=533, y=341) #para clicar em "vendas por especie"
pyautogui.press("enter")
time.sleep(3)

#para extrair o PDF

#selecionar a data de inicio 
pyautogui.click(x=532, y=212) #abrir calendario 
pyautogui.click(x=453, y=367) #selecionar data de hoje
#selecionar a data de fim 
pyautogui.click(x=532, y=229) #abrir calendario 
pyautogui.click(x=455, y=389) #selecionar data de hoje

#extraindo o PDF 
time.sleep(2)
pyautogui.click(x=793, y=577) #abrindo a opção para pdf
pyautogui.click(x=690, y=623) #selecionando a opção pdf
time.sleep(2)
pyautogui.click(x=852, y=579) #gerando relatorio
time.sleep(6
)
pyautogui.press("enter") #clicando em salvar

#abrir o pdf
time.sleep(5)
os.startfile(r"C:\Vendas por Espécie.pdf")


'''#para descobrir a coordenada 
time.sleep(5)
print(pyautogui.position())'''



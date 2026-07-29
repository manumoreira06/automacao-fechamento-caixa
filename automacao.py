import pyautogui
import os 
import time

#abriri o sistema gdoor 
os.startfile(r"C:\Caminho\Para\Gdoor.exe")
time.sleep(5)

#sequencia até gerar o pdf 
pyautogui.click(x,y) #descobrir as coordenadas para "relatórios"
#descobrir se vou prucurar "vendas por especie no canto ou se vou 
# mandar escrever, por enquanto vou seguir com a opção de escrever"
pyautogui.click(x,y)#clicar em localizar relatorio 
pyautogui.write("Venda por especie")
pyautogui.press("tab")
pyautogui.press("enter")

#para descobrir a coordenada 
time.sleep(5)
print(pyautogui.position())



import pyautogui
import time
import pandas as pd

# parte 1
pyautogui.press("win")
time.sleep(2)
pyautogui.write("chro")                                          
time.sleep(2)
pyautogui.press("enter")

time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)

pyautogui.doubleClick(x=802, y=403)
time.sleep(0.5)
pyautogui.write("meuemail@gmail.nãoteinteressa")
time
time.sleep(2)
pyautogui.press("TAB")
time.sleep(2)
pyautogui.write("747")
time.sleep(2)
pyautogui.press("TAB")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=751, y=292)
time.sleep(2)
tabela = pd.read_csv("produtos.csv")
print(tabela)

# parte 2
for linha in tabela.index:
    time.sleep(2)
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    time.sleep(2)
    pyautogui.press("TAB")
    time.sleep(2)
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    time.sleep(2)
    pyautogui.press("TAB")
    time.sleep(2)
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    time.sleep(2)
    pyautogui.press("TAB")
    time.sleep(2)
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    time.sleep(2)
    pyautogui.press("TAB")
    time.sleep(2)
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    time.sleep(2)
    pyautogui.press("TAB")
    time.sleep(2)
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    time.sleep(2)
    pyautogui.press("TAB")
    time.sleep(2)   
    obs = tabela.loc[linha,"obs"]
    if  not pd.isna(obs):
        pyautogui.press("TAB")
    time.sleep(2)   
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    time.sleep(2)       
    pyautogui.click(x=640, y=254) 
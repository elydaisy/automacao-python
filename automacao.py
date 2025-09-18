#pyautogui -> biblioteca para controlar o mouse e o teclado (faz automacoes)

import pyautogui
# pip install pyautogui
import time

#pyautogui.click --> clicar com o mouse
#pyautogui.press --> apertar uma unica tecla
#pyautogui.write --> escrever um texto
#pyautogui.hotkey --> apertar uma combinacao de teclas ex: #pyautogui.hotkey("ctrl", c)

pyautogui.PAUSE = 0.5 #coloca uma pausa de 1 segundo entre cada comando


#passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#abrir o chrome: 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click (x=1062, y=489)
pyautogui.PAUSE = 0.5
pyautogui.click (x=160, y=59)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) #esperar 3 segundos para a pagina carregar

#passo 2: fazer login
pyautogui.click (x=683, y=375) # clicar no campo de email
pyautogui.write("elyfake@gmail.com")

#preencgher a senha
pyautogui.press("tab") # apertar tab para ir para o campo de senha
pyautogui.write("sua senha")

#botao entrar
pyautogui.press("tab") # apertar tab para ir para o botao entrar
pyautogui.press("enter") # apertar enter para clicar no botao entrar

time.sleep(3) #esperar 3 segundos para a pagina carregar



#passo 3: importar a base de dados
import pandas 
tabela= pandas.read_csv("produtos.csv") # ler a base de dados na variavel tabela
print(tabela)   


#passo 4: cadastrar os produtos

#for linha intabela.Index --> para cada linha na tabela fazer


for linha in tabela.index: # para cada linha na tabela fazer... i index é o numero da linha
    pyautogui.click(x=808, y=261) # clicar no botao produtos

    codigo= tabela.loc[linha, "codigo"] # pegar o codigo do produto na linha atual
    pyautogui.write(codigo) # escrever o codigo do produto

    pyautogui.press("tab")
    marca= tabela.loc[linha, "marca"] # pegar a marca do produto na linha atual
    pyautogui.write(marca) # escrever a marca do produto

    pyautogui.press("tab")
    tipo= tabela.loc[linha, "tipo"] # pegar o tipo do produto na linha atual
    pyautogui.write(tipo) # escrever o tipo do produto

    pyautogui.press("tab")
    categoria= str(tabela.loc[linha, "categoria"]) # pegar a categoria do produto na linha atual -- transformar num em texto -> str(categoria)
    pyautogui.write(categoria) # escrever a categoria do produto

    pyautogui.press("tab")
    preco_unitario=  str(tabela.loc[linha, "preco_unitario"]) # pegar o preco unitario do produto na linha atual
    pyautogui.write(preco_unitario) # escrever o preco unitario do produto

    pyautogui.press("tab")
    custo= str(tabela.loc[linha, "custo"]) # pegar o custo do produto na linha atual
    pyautogui.write(str(custo)) # escrever o custo do produto

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"]) # pegar a obs do produto na linha atual
    
    if obs != "nan": # se a obs for diferente de nan (se tiver alguma obs)
        pyautogui.write(obs) # escrever a obs do produto
    
    pyautogui.press("tab")
    pyautogui.press("enter") # clicar no botao salvar


    pyautogui.scroll(10000 ) # o numero é o tamanho do scroll q vai rolar
    #passo 5: repetir para todos os produtos










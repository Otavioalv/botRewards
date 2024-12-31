import asyncio;
import pygetwindow;
import pyautogui;
import string;
import random;
import pyperclip;
import os;

# criar exe
# pyinstaller --onefile --icon=meu_icone.ico nome_do_seu_script.py
# dimensão icone, 16, 48, 256

# venv\Scripts\activate

async def runApp():
    rewars = "https://rewards.bing.com/?ref=pinML2BFG&OCID=PINREW";
    bing = "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx";
    
    
    while True:
        off = input("Deseja desligar o PC [y, n]: ");
        
        if off == "y" or off == "Y" or off == "n" or off == "N":
            break
        else:
            print("valor invalido");
    
    
    await openEdge(rewars); # Abre o edge
    
    isEqual = await selectWordAndCompare(1425, 740, 1660, 740, "Enquete do Rewards de hoje");
    
    # clica na terceira opção
    await posMouse(1530, 740, 'left', 5)
    
    # se for enquete, ele responde a posição de forma aleatoria
    if isEqual:
        await chosePosition(1200, 900, 1200, 960, "left");
    
    
    await posMouse(290, 20); # volta para a primeira janela
    await posMouse(540, 730, timer=8);  # clica na primeira opção 
    
    await posMouse(290, 20); # volta para a primeira janela
    await posMouse(1160, 730, timer=8); # clica na segunda opção
    
    await posMouse(290, 20); # volta para a primeira janela
    await posMouse(540, 10); # clica na segunda janela aberta
    
    await posMouse(400, 140, timer=2); # posiciona o mouse na barra de pesquisa
    
    await searchEdge(await randomWord()); # pesquisa de teste
    await searchEdgeMult(30, 20);
    
    await posMouse(1895, 15, timer=3); # aperta no X pra fechar o navegador
    
    if off == "y" or off == "Y":
        await powerOffPc();
    elif off == "n" or off == "N":
        print("Nao desligar");

async def openEdge(url):
    edgeDir = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe";
    
    process = await asyncio.create_subprocess_exec(edgeDir, url);
    
    await process.communicate();
    
    await asyncio.sleep(15);
    # config window edge;
    # windowns = pygetwindow.getAllTitles();
    # print(windowns);
    
    windowName = 'Microsoft Rewards - Pessoal — Microsoft\u200b Edge';
    try: 
        edge_window = pygetwindow.getWindowsWithTitle(windowName)[0];
        edge_window.activate();
        edge_window.maximize();
        print(f"\nJanela encontrada\n");
    except IndexError: 
        print(f"\nErro ao encontrar janela >>> {windowName}\n");

# pocisiona o mouse, clica e espera uns segundos
async def posMouse(posX, posY, btt='left', timer = 5, action='click'):
    # posiciona o mouse
    pyautogui.moveTo(posX, posY);

    await asyncio.sleep(.7);
    
    # clica com botao
    if action == "click":
        pyautogui.click(button=btt); 
    elif action == "down":
        pyautogui.mouseDown(button=btt); 

    
    await asyncio.sleep(timer);
 
async def searchEdge(text):
    pyautogui.write(text);
    await asyncio.sleep(.5);
    pyautogui.press('enter');
    await asyncio.sleep(.5);

async def posMouseNow(): 
    while True:
        x, y = pyautogui.position();
        print(f"X: {x} Y: {y}");

async def selectAllAndDelete():
    pyautogui.hotkey('ctrl', 'a');
    await asyncio.sleep(.7);
    pyautogui.press('backspace');
    await asyncio.sleep(.7);

async def searchEdgeMult(val, time): 
    await asyncio.sleep(2)
    
    for qtd in range(val):
        await posMouse(255, 150, 'left', 2);
        await selectAllAndDelete(); 
        sentence = await randomWord();
        await searchEdge(sentence);
        await asyncio.sleep(time);

async def randomWord():
    numberWord = random.randint(2, 8);

    allLyrics = string.ascii_lowercase;
    sentence = '';
    
    print("number: ", numberWord);
    for word in range(numberWord):
        numberLyrics = random.randint(2, 10);
        sentence += ''.join(random.choice(allLyrics) for i in range(numberLyrics)) + " ";

    await asyncio.sleep(.5);
    
    return sentence;

async def movMouse(num):
    pyautogui.scroll(num);

async def selectWordAndCompare(sPosX, sPosY, ePosX, ePosY, sentence):
    await asyncio.sleep(.7);
    
    await posMouse(sPosX, sPosY, 'left', 1, 'down');
    await posMouse(ePosX, ePosY, 'none', 1, 'none');
    
    await asyncio.sleep(.7);
    
    pyautogui.hotkey('ctrl', 'c');
    
    copyWord = pyperclip.paste();
    print(copyWord, sentence);
    if copyWord == sentence:
        return True;

    return False;
    
async def chosePosition(sPosX, sPosY, ePosX, ePosY, action):
    if(random.randint(0, 1)):
        await posMouse(sPosX, sPosY, action, 3);
    await posMouse(ePosX, ePosY, action, 3);

async def powerOffPc():
    for i in range(5):
        await asyncio.sleep(1);
        print(f"Desligando sistema em: {5-i}");
        
    await asyncio.sleep(1);
    os.system("shutdown /s /t 0")

if __name__ == '__main__':
    asyncio.run(runApp());
    # asyncio.run(posMouseNow())
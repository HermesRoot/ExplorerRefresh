import os
import time
import subprocess
import win32com.client
import pyautogui  
import pyperclip  
import urllib.parse  

def get_open_explorer_tabs():
    """Obtém os diretórios abertos no Explorer antes de reiniciá-lo."""
    explorer = win32com.client.Dispatch("Shell.Application")
    windows = explorer.Windows()
    paths = []

    for window in windows:
        if window.Name == "Explorador de Arquivos":
            # Pega a URL bruta e substitui os prefixos
            raw_url = window.LocationURL.replace("file:///", "").replace("/", "\\")
            # Decodifica a URL com urllib.parse.unquote e depois força cp1252 para caracteres locais
            path = urllib.parse.unquote(raw_url, encoding='cp1252')
            paths.append(path)
    
    return paths

def reopen_explorer_tabs(paths):
    """Reabre as abas no Explorer."""
    if not paths:
        return

    # Abre a primeira aba diretamente
    subprocess.Popen(f'explorer "{paths[0]}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)

    # Reabre as demais abas
    for path in paths[1:]:
        pyautogui.hotkey('ctrl', 't')  # Nova aba
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')  # Foca na barra de endereço
        time.sleep(1)
        
        # Copia o caminho com codificação cp1252
        pyperclip.copy(path.encode('cp1252', errors='replace').decode('cp1252'))
        pyautogui.hotkey('ctrl', 'v')  # Cola o caminho
        time.sleep(1)
        pyautogui.press('enter')  # Abre o diretório
        time.sleep(2)

if __name__ == "__main__":
    # Obtém os diretórios abertos
    open_explorer_dirs = get_open_explorer_tabs()
    print("Caminhos detectados:", open_explorer_dirs)  # Para depuração

    # Fecha o Explorer
    subprocess.run("taskkill /f /im explorer.exe", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)

    # Reabre o Explorer
    subprocess.Popen("explorer.exe", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)

    # Reabre as abas
    reopen_explorer_tabs(open_explorer_dirs)
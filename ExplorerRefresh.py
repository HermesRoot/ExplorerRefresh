import os
import time
import subprocess
import win32com.client
import pyautogui  # `pip install pyautogui`
import pyperclip  # `pip install pyperclip`

def get_open_explorer_tabs():
    """Obtém os diretórios abertos no Explorer antes de reiniciá-lo."""
    explorer = win32com.client.Dispatch("Shell.Application")
    windows = explorer.Windows()
    paths = []

    for window in windows:
        if window.Name == "Explorador de Arquivos":
            path = window.LocationURL.replace("file:///", "").replace("/", "\\") 
            paths.append(path)
    
    return paths

if __name__ == "__main__":
    open_explorer_dirs = get_open_explorer_tabs()

    subprocess.run("taskkill /f /im explorer.exe", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)

    subprocess.Popen("explorer.exe", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)

    if open_explorer_dirs:
        subprocess.Popen(f'explorer "{open_explorer_dirs[0]}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2) 

        for path in open_explorer_dirs[1:]:
            pyautogui.hotkey('ctrl', 't') 
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'l') 
            time.sleep(1)
            pyperclip.copy(path) 
            pyautogui.hotkey('ctrl', 'v')  
            time.sleep(1)
            pyautogui.press('enter')  
            time.sleep(2)  

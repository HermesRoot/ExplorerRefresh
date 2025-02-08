# 🚀 ExplorerRefresh

Este projeto contém um script em Python para reiniciar o Explorador de Arquivos do Windows 11 sem perder as abas abertas.

## 📌 Sobre o Projeto
O Windows 11 introduziu abas no Explorador de Arquivos, mas não oferece uma opção nativa para restaurá-las após reiniciar o `Explorer.exe`. Este script resolve esse problema capturando as abas abertas antes do fechamento e reabrindo-as corretamente.

> **⚠️ Nota:**  
> Atualmente, existe um problema ao restaurar abas cujo caminho contenha caracteres acentuados (á, é, í, ó, ú, ç, etc.) ou hífens (`-`). O Windows pode não reconhecer corretamente esses caminhos ao colá-los no Explorer, fazendo com que a pasta seja aberta incorretamente ou apenas até o diretório raiz.

## 📂 Estrutura do Projeto
```
ExplorerRefresh/
|── ExplorerRefresh.py   # Script principal
|── ExplorerRefresh.vbs  # Atalho para rodar o script sem abrir terminal
|── requirements.txt     # Lista de dependências
|── README.md            # Informações sobre o projeto
|── LICENSE              # Licença do projeto
```

## 🛠️ Como Usar
### 1⃣ Instale as dependências necessárias
Execute o seguinte comando para instalar todas as bibliotecas usadas no script:  
```bash
pip install -r requirements.txt
```
Caso prefira instalar manualmente, execute:  
```bash
pip install pyautogui pywin32 pyperclip
```

### 2⃣ Execute o script
```bash
python ExplorerRefresh.py
```

### 3⃣ Utilize o atalho `.vbs` (opcional)  
Para evitar que o terminal apareça ao executar o script, utilize o arquivo `ExplorerRefresh.vbs`.  
> **⚠️ Importante:** Antes de usar, edite o arquivo `ExplorerRefresh.vbs` e substitua `C:\Caminho\Para\ExplorerRefresh.py` pelo caminho correto onde o script está salvo:
> ```vbs
> Set objShell = CreateObject("WScript.Shell")
> objShell.Run "pythonw C:\Caminho\Para\ExplorerRefresh.py", 0, False
> ```

## ⚡ Funcionalidades
✅ Obtém as abas abertas no Explorer antes de fechá-lo.  
✅ Fecha e reinicia o Explorer sem exibir mensagens.  
✅ Restaura todas as abas corretamente na mesma janela.  

## 📄 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

## 💡 Contribuição
Sugestões e melhorias são bem-vindas!  
Sinta-se à vontade para **forkar, modificar e contribuir**.  

---
Criado por **HermesRoot** 🤯

# ExplorerRefresh

Este projeto contém um script em Python para reiniciar o Explorador de Arquivos do Windows 11 sem perder as abas abertas.

## 📌 Sobre o Projeto

O Windows 11 introduziu abas no Explorador de Arquivos, mas não oferece uma opção nativa para restaurá-las após reiniciar o `Explorer.exe`. Este script resolve esse problema capturando as abas abertas antes do fechamento e reabrindo-as corretamente.

Agora, o script também corrige problemas de encoding ao restaurar abas que contenham caracteres acentuados (á, é, í, ó, ú, ç, etc.) ou hífens (`-`). Isso foi resolvido com `urllib.parse.unquote()`, garantindo que os caminhos sejam interpretados corretamente pelo Windows.

## 🛠️ Como Usar

### 1. Instale as dependências necessárias

Execute o seguinte comando para instalar todas as bibliotecas usadas no script:  

```bash
pip install -r requirements.txt
```

Caso prefira instalar manualmente, execute:

```bash
pip install pyautogui pywin32 pyperclip
```

### 2. Execute o script

```bash
python ExplorerRefresh.py
```

## ⚡ Funcionalidades

✅ Obtém as abas abertas no Explorer antes de fechá-lo.

✅ Fecha e reinicia o Explorer.

✅ Corrige problemas de encoding ao restaurar abas com caracteres especiais.

✅ Melhor estruturação na reabertura de abas, garantindo maior estabilidade.

✅ Otimização de tempos de espera entre ações do script.  

## 📝 Licença

Este projeto está licenciado sob a licença **MIT** — veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

Desenvolvido por **HermesRoot**.  

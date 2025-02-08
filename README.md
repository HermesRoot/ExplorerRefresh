# ExplorerRefresh
Script em Python para reiniciar o Explorer no Windows 11 sem perder abas abertas. Ele captura as abas antes do fechamento e as restaura corretamente.

# 🚀 ExplorerRefresh

Este projeto contém um script em Python para reiniciar o Explorador de Arquivos do Windows 11 sem perder as abas abertas.

## 📌 Sobre o Projeto
O Windows 11 introduziu abas no Explorador de Arquivos, mas não oferece uma opção nativa para restaurá-las após reiniciar o Explorer.exe. Este script resolve esse problema capturando as abas abertas antes do fechamento e reabrindo-as corretamente.

## 📂 Estrutura do Projeto
```
ExplorerRefresh/
│── ExplorerRefresh.py   # Script principal
│── ExplorerRefresh.vbs  # Atalho para rodar o script sem abrir terminal
│── README.md            # Informações sobre o projeto
│── LICENSE              # Licença do projeto
```

## 🛠️ Como Usar
1. Instale a dependência necessária:
   ```bash
   pip install pyautogui
   ```
2. Execute o script:
   ```bash
   python ExplorerRefresh.py
   ```
3. Para facilitar a execução, use o arquivo `.vbs` para rodar o script sem abrir o terminal.

## ⚡ Funcionalidades
- Obtém as abas abertas no Explorer antes de fechá-lo.
- Fecha e reinicia o Explorer sem exibir mensagens.
- Restaura todas as abas corretamente na mesma janela.

## 📄 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

## 💡 Contribuição
Sugestões e melhorias são bem-vindas! Feel free to fork, modificar e contribuir.

---
Criado por HermesRoot 😉

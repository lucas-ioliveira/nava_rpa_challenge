# 🤖 Nava RPA Challenge (Teste de código)

Este projeto é uma solução automatizada para o [RPA Challenge](https://rpachallenge.com/), desenvolvida em **Python**. O robô lê dados de uma planilha Excel e preenche dinamicamente um formulário web onde os campos mudam de posição a cada submissão, testando a resiliência e a precisão da automação.

<br>

## 📂 Estrutura do Projeto

```text
nava_rpa_challenge/
├── src/
│   ├── logs/               # Gerado automaticamente pelo robô (.log)
│   ├── resources/          # Planilhas de entrada (ex: challenge.xlsx)
│   ├── screenshots/        # Evidências geradas no final do processo
│   ├── services/
│   │   ├── consumer.py     # Lógica de automação web (Playwright)
│   │   └── handler.py      # Lógica de manipulação de dados (OpenPyXL)
│   └── utils/
│       └── logger.py       # Configuração do Logger central
├── venv/                   # Ambiente virtual
├── .env                    # Variáveis de ambiente (URL)
├── main.py                 # Arquivo principal (Entrypoint)
└── README.md               # Documentação do projeto
```

<br>

<h2>Pré-requisitos</h2>

- [Python](https://www.python.org/)

<br>

<h2>Clone</h2>

Como clonar o projeto:

```bash
git clone https://github.com/lucas-ioliveira/nava_rpa_challenge.git
```

<br>

<h2 id="started">🚀 Primeiros passos</h2>

- Atualizar o arquivo .env_exemplo para .env

- Criar o ambiente virtual e ativar (Linux)

```bash
python3 -m venv venv
source venv/bin/activate
```

- Windows

```bash
python -m venv venv
venv\bin\activate
```

- Instalar as dependências

```bash
pip install -r requirements.txt
```
- Instale o motor de navegadores do Playwright (Obrigatório)

```bash
playwright install chromium
```

<br>

## ✨ Execução

```bash
python main.py
```

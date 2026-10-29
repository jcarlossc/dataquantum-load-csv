# DataQuantum Load CSV

Leitura de arquivos CSV com Python e Pandas, com validação do caminho, registro de logs e tratamento de exceções.

[![CI](https://github.com/jcarlossc/dataquantum-load-csv/actions/workflows/ci.yml/badge.svg)](https://github.com/jcarlossc/dataquantum-load-csv/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/dataquantum-load-csv.svg)](https://badge.fury.io/py/dataquantum-load-csv)
[![Python](https://img.shields.io/pypi/pyversions/dataquantum-load-csv)](https://pypi.org/project/dataquantum-load-csv/)
[![License: MIT](https://img.shields.io/badge/Licença-MIT-blue.svg)](LICENSE)

## 📌 Sobre o projeto

O **DataQuantum Load CSV** é uma biblioteca Python desenvolvida para simplificar a leitura de arquivos CSV em projetos de análise e engenharia de dados.

O pacote utiliza o Pandas para carregar os dados em um DataFrame, permitindo configurar o delimitador e a codificação do arquivo.

### Principais recursos

- Leitura de arquivos CSV com Pandas.
- Configuração do delimitador e da codificação.
- Verificação da existência do arquivo.
- Registro de eventos por meio do módulo `logging`.
- Tratamento e propagação de exceções.
- Testes automatizados com Pytest.
- Verificação de qualidade com Ruff e MyPy.
- Integração contínua com GitHub Actions.

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- Poetry
- Taskipy
- Pytest
- Pytest-Cov
- Ruff
- MyPy
- Pre-commit
- GitHub Actions
- Release-please

## 📦 Instalação

Instale o pacote publicado no PyPI:

```bash
pip install dataquantum-load-csv
```
ou

```bash
poetry add dataquantum-load-csv
```

Para desenvolvimento local, clone o repositório:

```bash
git clone https://github.com/jcarlossc/dataquantum-load-csv.git
cd dataquantum-load-csv
```

Instale as dependências, incluindo as dependências de desenvolvimento:

```bash
poetry install --with dev
```

> **Observação:** a instalação via PyPI depende da publicação do pacote. Ajuste o endereço do repositório e o nome do pacote caso sejam diferentes no projeto final.

## 🚀 Como utilizar

```python
from dataquantum_load_csv import get_load_csv

df = load_csv("data/vendas.csv")

print(df.head())
print(df.shape)
```

### Definindo delimitador e codificação

```python
from dataquantum_load_csv import get_load_csv

df = load_csv(
    file_csv="data/vendas.csv",
    sep=";",
    encoding="utf-8",
)

print(df.head())
```

O parâmetro `sep` define o separador das colunas, enquanto `encoding` especifica a codificação usada na leitura do arquivo.

## ⚙️ Parâmetros da função

| Parâmetro | Tipo | Padrão | Descrição |
|---|---|---|---|
| `file_csv` | `str` | Obrigatório | Caminho do arquivo CSV. |
| `sep` | `str` | `","` | Delimitador das colunas. |
| `encoding` | `str` | `"utf-8"` | Codificação do arquivo. |

**Retorno:** `pandas.DataFrame` com os dados carregados.

## 🛡️ Tratamento de erros

A função utiliza blocos `try/except` para registrar os erros e propagar as exceções ao código que a chamou.

| Exceção | Quando ocorre |
|---|---|
| `FileNotFoundError` | O arquivo informado não existe. |
| `pandas.errors.EmptyDataError` | O arquivo não contém dados ou cabeçalhos que possam ser lidos. |
| `pandas.errors.ParserError` | O Pandas não consegue interpretar a estrutura do CSV. |
| `UnicodeDecodeError` | A codificação especificada não permite decodificar o arquivo. |
| `Exception` | Outros erros inesperados durante a leitura. |

### Exemplo de captura de erros

```python
from pathlib import Path

import pandas as pd

from dataquantum_load_csv import get_load_csv

try:
    df = load_csv("data/vendas.csv")
except FileNotFoundError:
    print("Arquivo CSV não encontrado.")
except pd.errors.EmptyDataError:
    print("O arquivo está vazio ou não possui cabeçalho válido.")
except pd.errors.ParserError:
    print("Não foi possível interpretar a estrutura do CSV.")
except UnicodeDecodeError:
    print("Não foi possível decodificar o arquivo.")
except Exception as exc:
    print(f"Erro inesperado: {exc}")
else:
    print("Arquivo carregado com sucesso.")
```

A biblioteca registra os detalhes técnicos dos erros por meio do `logging` e utiliza `raise` para que o programa chamador possa decidir como reagir.

## 🧾 Registro de logs

O pacote utiliza o módulo padrão `logging` para registrar o início da leitura, o resultado do carregamento e as exceções encontradas.

Exemplo de configuração no programa que utiliza a biblioteca:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
```

Os registros podem incluir informações sobre o arquivo processado, a quantidade de linhas e colunas e os erros ocorridos.

**Atenção:** configure o sistema de logs da aplicação consumidora para visualizar as mensagens no console ou encaminhá-las para um arquivo.

## 🧪 Testes automatizados

Execute todos os testes:

```bash
poetry run task pytest
```

Execute os testes com relatório de cobertura:

```bash
poetry run task covhtml
```

O objetivo é verificar o comportamento esperado da função, incluindo a leitura correta dos arquivos e o tratamento de erros.

## 🔍 Qualidade de código

Execute as verificações configuradas no projeto:

```bash
poetry run task lint
```

Esse comando executa as tarefas de qualidade definidas no `pyproject.toml`. Dependendo da configuração, elas podem incluir Ruff, formatação e MyPy.

Para executar as verificações individualmente:

```bash
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy src
```

Para corrigir automaticamente problemas de lint:

```bash
poetry run ruff check . --fix
```

## 🪝 Pre-commit

Execute os hooks configurados em todos os arquivos:

```bash
poetry run pre-commit run --all-files
```

Caso algum hook modifique arquivos, revise as alterações e execute o comando novamente antes de criar o commit.

## ⚡ Comandos Taskipy

Os comandos abaixo pressupõem que as tarefas correspondentes estejam definidas na seção `[tool.taskipy.tasks]` do `pyproject.toml`.

| Comando | Finalidade |
|---|---|
| `poetry run task lint` | Verifica a qualidade do código. |
| `poetry run task test` | Executa os testes automatizados. |
| `poetry run task covhtml` | Executa os testes com cobertura. |
| `poetry run task covcmd` | Executa os testes e mostra no console. |
| `poetry run task --list` | Lista as tarefas disponíveis, conforme a versão e configuração do Taskipy. |

Consulte o `pyproject.toml` para confirmar os nomes exatos das tarefas configuradas no projeto.

## 📂 Estrutura do projeto

```text
dataquantum-load-csv/
├── src/
│   └── dataquantum_load_csv/
│       ├── __init__.py
│       └── load_csv.py
├── tests/
│   └── test_load_csv.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .pre-commit-config.yaml
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml
└── README.md
```

## 🔄 Integração contínua

O projeto pode utilizar GitHub Actions para executar automaticamente as verificações configuradas a cada push ou pull request.

As verificações podem incluir:

- Instalação das dependências.
- Execução dos testes.
- Análise estática e formatação.
- Verificação de tipos.
- Validação dos hooks de pre-commit.

O badge de CI no início deste documento mostra o estado do workflow configurado no repositório.

## 🗺️ Melhorias futuras

- Detecção automática de delimitador e codificação.
- Validação de colunas obrigatórias.
- Verificação de tipos de dados.
- Tratamento de valores ausentes.
- Relatórios detalhados de erros de leitura.

## 🤝 Contribuições

Contribuições são bem-vindas. Para propor uma melhoria:

1. Crie um fork do repositório.
2. Crie uma branch para sua alteração.
3. Implemente a melhoria e adicione testes.
4. Execute os testes e as verificações de qualidade.
5. Envie um pull request.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

## 👨‍💻 Autor

**DataQuantum**

Desenvolvimento de soluções em análise, ciência e engenharia de dados.

- GitHub: https://github.com/jcarlossc

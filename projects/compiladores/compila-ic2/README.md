# PRÉ REQUISITOS
ubuntu, vscode, python, pip, antlr

# TUTORIAL

### Criar ambiente virtual
virtualenv venv

### Ativar ambiente virtual
source venv/bin/activate

### Instalar requisitos do ambiente virtual
pip install -r requirements.txt

### Compilar em python
python3 -m vjj -h

### Testar arquivo.vjj FUNCIONANDO
python3 -m vjj input.vjj
python3 -m vjj zetta.vjj

### Testar arquivo.vjj COM ERRO
python3 -m vjj zetta.vjj

## Meu jeito de compilar
deletar todos os arquivos ".interp, .tokens, e .py" da pasta /parser, restando apenas o arquivo vjj.g4
depois executar

python3 -m vjj input.vjj

OU

python3 -m {nome_da_pasta}} {nome_arquivo}.txt

Exemplo - python3 -m vjj input.txt

# Exemplo do Evandro

https://gitlab.com/evandro-crr/vjj/-/tree/lambda

# Setup 

Install Python packages
```shell
pip install -r requirement.txt
```

> ANTLR requirers java to generate the parser.

# Usage

```shell
$ python -m vjj -h
usage: vjj [-h] [-o] input

C-- interpreter

positional arguments:
input      source code

optional arguments:
-h, --help  show this help message and exit
-o          python output
```

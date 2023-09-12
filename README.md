
[![Testes Automátizados](https://github.com/GuilhLopes/portf-lio-/actions/workflows/testes.yaml/badge.svg)](https://github.com/GuilhLopes/portf-lio-/actions/workflows/testes.yaml)

# Portfólio
Nesse portfólio conterá todos os arquivos que constroem o site.
# Guia de instalação

Primeiramente devemos Clonar o repositório para sua maquina local com o comando pelo git bash:
```
git clone https://github.com/GuilhLopes/portf-lio-.git
```
A partir dai recomendados criar uma nova Branch para fazer as alterações sem ter o risco para dar erros no codigo da main:
```
git checkout -b 'nome da branch'
```
### Criando o ambiente virtual

Após a criação de uma nova branch no seu repositório local, iremos criar um ambiente virtual (.venv) e instalar as dependencias do projeto nesse ambiente.

Para a criação do ambiente virtual utilizamos no cmd: 
```
python -m venv env
```
Após a criação devemos ativar o ambiente virtual:

Código cmd:
```
.\env\Scripts\Activate.bat
```
Código PowerShell:

```
.\env\Scripts\Activate.ps1
```
Antes de irmos para o proximo passa certifique-se que o ambiente virtual está ativo, no seu cmd ou powershell devem estar com o caminho:
```
(env) C:\Users\Usuário\Desktop\Portifólio\portf-lio->
```

Note que o caminho pode ser diferente, mais tevemos ter o ***(env)*** no começo do caminho.

### Instalando dependencias

Pronto, agora que temos o nosso ambiente virtual, podemos instalar as dependencias do nosso projeto utilizando:
```
pip install -r requirements.txt
```

Ao final desse comando poderemos ir no arquivo **run.py** e rodar o site no localHost.

# Organização dos arquivos

- *Arquivos em HTML:* Todos os arquivos HTML estarão na pasta */templates*.

- *Arquivos app e run:* Estarão no pasta principal do repositório, e o arquivo run.py é utilizado para rodar o site e o app.py são as configurações das rotas.

- *Arquivos de imagem:* O caminho pra os arquivos de imagem é */static/imagens*, nessa pasta estarão todos os arquivos de imagens utilizados.

- *Arquivo de testes:* Esses arquivos estarão na pasta */tests*, serão os arquivos que farão o teste das funcionalidades.

# Fluxo de trabalho do Actions

- Passo 1: irá criar uma maquina virtual ubuntu para rodar os códigos.
- Passo 2: irá criar todos os arquivos do reposotório para a maquina virtual.
- Passo 3: irá instalar e configurar o python na versão 3.11.4 para rodar os arquivos.
- Passo 4: fará a instalação das dependencias do python de acordo com o *requirements.txt*.
- Passo 5: Utilizará o pytest para fazer os testes configurados na pasta *tests*.

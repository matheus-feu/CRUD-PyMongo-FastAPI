[![wakatime](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/2b340b09-9039-4bfc-a6c3-e61e49baaa3e.svg)](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/2b340b09-9039-4bfc-a6c3-e61e49baaa3e)

# Pymongo com FastAPI - CRUD Bookstore

Esta API é uma simples aplicação de CRUD de uma livraria, utilizando FastAPI e MongoDB.

## Rodando a aplicação

Setar as variáveis de ambiente no arquivo `.env`, trocar os valores de acordo com o seu ambiente.

```bash
# Base
APP_VERSION=
APP_V1_PREFIX=
PROJECT_NAME=
PROJECT_DESCRIPTION=
# Database
MONGODB_URI=
MONGODB_NAME=
```

Instalar as dependências do projeto, estou utilizando o Poetry como gerenciador de pacotes.

```bash
poetry install
```

Iniciar o servidor, por padrão ele irá rodar na porta 8000.

```bash
python main.py
```

O banco de dados está sendo executado em um container Docker, para subir o container basta executar o comando abaixo.

```bash 
docker-compose up -d
```

## Documentação

A documentação da API está disponível em `/docs` ou `/redoc`.
Acessando link: http://localhost:8000/docs

![Swagger](https://imgur.com/tAjwTuM.png)
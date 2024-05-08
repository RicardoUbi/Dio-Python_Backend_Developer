# Criando Uma API Com FastAPI Utilizando TDD
## StoreApi

Esta é uma API de cadastro de produtos chamada StoreAPI. É uma API pequena desenvolvida para aprender na prática como implementar o TDD em uma aplicação utilizando FastAPI juntamente com Pytest.


## Tecnologias utilizadas:

* [Python](https://www.python.org/): linguagem de programação.
* [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/): Um framework web Python de alto desempenho para APIs RESTful.
* [pydantic](https://docs.pydantic.dev/latest/): Uma biblioteca para validação de dados e criação de modelos de dados.
* [docker](https://www.docker.com/): Uma plataforma de virtualização de nível de sistema que permite empacotar aplicativos e seus ambientes em contêineres.
* [MongoDB](https://www.mongodb.com/): Um banco de dados NoSQL.
* [Pytest](https://pytest.org/): Bibliteca para teste de software.

## Execução da API

Para executar o projeto, utilizei a venv.

Caso opte por usa-la, execute:

## Windows
```bash
python -m venv .venv
source .venv/bin/activate
```
## Linux
```bash
python3 -m venv .venv
.venv\Scripts\activate
```

Verifique se o ambiente virtual está ativo:
```bash
(venv) myproject
```
## Certifique-se de ter instalado poetry
Após instalado, execute:
```bash
poetry install
```

## Executando banco de dados

Para subir o banco de dados, caso não tenha o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
docker-compose up -d
```
Para verificar se subiu o banco de dados, execute:
```bash
docker ps
```

## API

Para subir a API, execute:
```bash
make run
```
e acesse: http://127.0.0.1:8000/docs

## Testes

Para realizar os testes, execute:
```bash
make test
```
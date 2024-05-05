# Desenvolvendo Primeira API com FastAPI, Python e Docker
## WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI. É uma API pequena desenvolvida para aprender o necessario sobre como utilizar o FastAPI.

O sistema permite cadastrar e pesquisar atletas, categorias e centros de treinamento, garantindo a precisão dos dados através de mecanismos de segurança contra duplicidades.


## Tecnologias utilizadas:

* [Python](https://www.python.org/): linguagem de programação
* [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/): Um framework web Python de alto desempenho para APIs RESTful.
* [alembic](https://readthedocs.org/projects/alembic/): Uma ferramenta de migração de banco de dados Python que facilita a criação, gerenciamento.
* [SQLAlchemy](https://docs.sqlalchemy.org/): Uma biblioteca de mapeamento objeto-relacional (ORM) Python que conecta o código da aplicação ao banco de dados. 
* [pydantic](https://docs.pydantic.dev/latest/): Uma biblioteca Python para validação de dados e criação de modelos de dados robustos.
* [postgres](https://www.postgresql.org/): Um sistema de gerenciamento de banco de dados relacional (SGBD).
* [docker](https://www.docker.com/): Uma plataforma de virtualização de nível de sistema que permite empacotar aplicativos e seus ambientes em contêineres leves e portáteis.


## Execução da API

Para executar o projeto, utilizei a venv.

Caso opte por usa-la, execute:

## Windows
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Linux
```bash
python3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Verifique se o ambiente virtual está ativo:
```bash
(venv) myproject
```
## Executando banco de dados

Para subir o banco de dados, caso não tenha o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
docker-compose up -d
```

```bash
alembic upgrade head
```

## API

Para subir a API, execute:
```bash
make run
```
e acesse: http://127.0.0.1:8000/docs


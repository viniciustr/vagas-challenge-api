# Desafio Técnico API VAGAS.com

## Sobre a aplicação

Esta aplicação usou o template Flask Api Starter Kit, disponível [aqui](https://github.com/antkahn/flask-api-starter-kit.git).

Ela implementa todos os endpoints solicitados no desafio técnico, utilizando uma arquitetura RESTful e documentada através do Swagger.

### Arquitetura

Ela está estruturada em containers Docker, utilizando o docker-compose para orquestrá-los. Os componentes são:

* Container Python: contém a API em si, implementada com o framework Flask e demais componentes;
* Container PostgreSQL: contém o banco de dados da aplicação, onde são armazenadas as tabelas com as pessoas, vagas e candidaturas, de acordo com os requisitos da API.

A aplicação Python está baseada no padrão MVC (Model View Controller) e está estruturada nas seguintes camadas:

* Routes: mapeia as rotas da aplicação (eg. `/v1/vagas`) aos recursos;
* Resources: são, em essência, os controllers da aplicação. Contêm a implementação dos verbos HTTP e direcionam para os services ou repositories adequados para atender suas respectivas requisições;
* Services: implementam as regras de negócio da aplicação. No caso, foi utilizada especialmente para a parte de candidaturas, pois envolvia o cálculo da menor distância e _score_ da candidatura (parâmetros *N* e *D*);
* Repositories: executam as operações de banco de dados necessárias para persistir e obter dados;
* Models: implementam as classes que modelam as tabelas do banco de dados, através do framework ORM SQLAlchemy. Dessa forma, não foi necessário criar nenhuma tabela ou consulta SQL manualmente.

### Versionamento de banco de dados

As alterações nos `models` descritos anteriormente envolviam, como consequência, alterações no banco de dados. Para controlar isso, a aplicação conta com o componente `alembic`, o qual cria _migrations_, isto é, scripts de versionamento do banco de dados. Ao inicializar a aplicação, basta executar todas as _migrations_ para chegar à versão mais recente do conjunto de tabelas do banco de dados.

## Botando para funcionar

Chega de papo! Vamos executar a aplicação!

Para isso, siga estes passos bem simples!

- Certifique-se que o Docker e Docker-compose estão instalados na sua máquina
- Clone este projeto
- Instale as dependências com o comando `$ make install` no diretório do projeto
- Aplique as migrações do banco de dados com o comando `$ make upgrade` no diretório do projeto
- Inicie a aplicação com o comando `$ make start`
- Acesse o Swagger do projeto [aqui](http://localhost:3000/apidocs)
- Pronto!

## Mais detalhes

Consulte a documentação abaixo para aprender o que mais pode ser feito no projeto!

# Documentação original do Flask Api Starter Kit

This starter kit is designed to allow you to create very fast your Flask API.

The primary goal of this project is to remain as **unopinionated** as possible. Its purpose is not to dictate your project structure or to demonstrate a complete sample application, but to provide a set of tools intended to make back-end development robust, easy, and, most importantly, fun.

This starter kit comes with a [tutorial](https://github.com/antkahn/flask-api-starter-kit/blob/tutorial/doc/installation.md).
Check it out if you want a quick tutorial on how to use Flask with this architecure.

## Table of Contents

1. [Dependencies](#dependencies)
1. [Getting Started](#getting-started)
1. [Commands](#commands)
1. [Database](#database)
1. [Application Structure](#application-structure)
1. [Development](#development)
1. [Testing](#testing)
1. [Lint](#lint)
1. [Swagger](#swagger)

## Dependencies

You will need [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).

## Getting Started

First, clone the project:

```bash
$ git clone https://github.com/antkahn/flask-api-starter-kit.git <my-project-name>
$ cd <my-project-name>
```

Then install dependencies and check that it works

```bash
$ make install      # Install the pip dependencies on the docker container
$ make start        # Run the container containing your local python server
```

If everything works, you should see the available routes [here](http://127.0.0.1:3000/application/spec).

The API runs locally on docker containers. You can easily change the python version you are willing to use [here](https://github.com/antkahn/flask-api-starter-kit/blob/master/docker-compose.yml#L4), by fetching a docker image of the python version you want.

## Commands

While developing, you will probably rely mostly on `make start`; however, there are additional scripts at your disposal:

| `make <script>` | Description                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| `install`       | Install the pip dependencies on the server's container.                      |
| `start`         | Run your local server in its own docker container.                           |
| `daemon`        | Run your local server in its own docker container as a daemon.               |
| `db/connect`    | Connect to your docker database.                                             |
| `db/migrate`    | Generate a database migration file using alembic, based on your model files. |
| `db/upgrade`    | Run the migrations until your database is up to date.                        |
| `db/downgrade`  | Downgrade your database by one migration.                                    |
| `test`          | Run unit tests with pytest in its own container.                             |
| `coverage`      | Run test coverage using pytest-cov.                                          |
| `lint`          | Run flake8 on the `src` and `test` directories.                              |
| `safety`        | Run safety to check if your vendors have security issues.                    |

## Database

The database is in [PostgreSql](https://www.postgresql.org/).

Locally, you can connect to your database using :

```bash
$ make db/connect
```

However, you will need before using this command to change the docker database container's name [here](https://github.com/antkahn/flask-api-starter-kit/blob/master/package.json#L6).

This kit contains a built in database versioning using [alembic](https://pypi.python.org/pypi/alembic).
Once you've changed your models, which should reflect your database's state, you can generate the migration, then upgrade or downgrade your database as you want. See [Commands](#commands) for more information.

The migration will be generated by the container, it may possible that you can only edit it via `sudo` or by running `chown` on the generated file.

## Application Structure

The application structure presented in this boilerplate is grouped primarily by file type. Please note, however, that this structure is only meant to serve as a guide, it is by no means prescriptive.

```
.
├── devops                   # Project devops configuration settings
│   └── deploy               # Environment-specific configuration files for shipit
├── migrations               # Database's migrations settings
│   └── versions             # Database's migrations versions generated by alembic
├── src                      # Application source code
│   ├── models               # Python classes modeling the database
│   │   ├── abc.py           # Abstract base class model
│   │   └── user.py          # Definition of the user model
│   ├── repositories         # Python classes allowing you to interact with your models
│   │   └── user.py          # Methods to easily handle user models
│   ├── resources            # Python classes containing the HTTP verbs of your routes
│   │   └── user.py          # Rest verbs related to the user routes
│   ├── routes               # Routes definitions and links to their associated resources
│   │   ├── __init__.py      # Contains every blueprint of your API
│   │   └── user.py          # The blueprint related to the user
│   ├── swagger              # Resources documentation
│   │   └── user             # Documentation of the user resource
│   │       └── GET.yml      # Documentation of the GET method on the user resource
│   ├── util                 # Some helpfull, non-business Python functions for your project
│   │   └── parse_params.py  # Wrapper for the resources to easily handle parameters
│   ├── config.py            # Project configuration settings
│   ├── manage.py            # Project commands
│   └── server.py            # Server configuration
└── test                     # Unit tests source code
```

## Development

To develop locally, here are your two options:

```bash
$ make start           # Create the containers containing your python server in your terminal
$ make daemon          # Create the containers containing your python server as a daemon
```

The containers will reload by themselves as your source code is changed.
You can check the logs in the `./server.log` file.

## Testing

To add a unit test, simply create a `test_*.py` file anywhere in `./test/`, prefix your test classes with `Test` and your testing methods with `test_`. Unittest will run them automaticaly.
You can add objects in your database that will only be used in your tests, see example.
You can run your tests in their own container with the command:

```bash
$ make test
```

## Lint

To lint your code using flake8, just run in your terminal:

```bash
$ make lint
```

It will run the flake8 commands on your project in your server container, and display any lint error you may have in your code.

## Swagger

Your API needs a description of it's routes and how to interact with them.
You can easily do that with the swagger package included in the starter kit.
Simply add a docstring to the resources of your API like in the `user` example.
The API description will be available [here](http://127.0.0.1:3000/application/spec).

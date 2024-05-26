# Postm

Postm é a implementação do projeto final do processo seletivo da Loading.

# Sobre o projeto

Como dito pela própia Loading:

> O objetivo deste desafio é avaliar suas habilidades de desenvolvimento back-end, especificamente na criação de uma API REST para gerenciamento de postagens. A API permitirá que os usuários realizem operações CRUD (Create, Read, Update, Delete).

# Como executar essa API?

> Perdoem-me. Ainda não sei utilizar docker para facilitar a sua instalação. 

Para continuar você precisará ter o [python](https://www.python.org/), [poetry](https://python-poetry.org/) e o [mongoDB](https://www.mongodb.com/) instalados em sua máquina.

1. Clone o repositório:
```bash
git clone https://github.com/pab-h/postm.git
```

2. Instale as dependencias utilizando o **poetry**:
```bash
poetry install 
```

3. Crie e preencha corretamente o arquivo com as variáveis de ambiente, *.env*, Há um arquivo exemplo, *.env-example*.

4. (opcional) Execute os testes unitários para verificar se está tudo certo

```bash
poetry run test 
```

5. Inicialize a aplicação:

```bash
poetry run start 
```

# Documentação 

A documentação dos endpoints que essa API oferece estão [disponíveis aqui, via Postman](https://documenter.getpostman.com/view/23833771/2sA3Qqgsjr).

# Trabalho de Computação Distribuída

### Alunos
- Arthur M
- Gabriel Willye

### Tecnologias
| Nome      | Versão |
| :-------: | :----: |
| Python    | 3.9    |
| Mysql     | 8.0    |


___

### Como executar

<p style="color: orange">Necessário o Docker instalado com o Docker compose</p>

#### Passo 1

Criar arquivo `/docker/.env` e preencher as variáveis de ambiente.

```env
# Preencher as variáveis de ambiente
SECRET_KEY='secret_key'
DATABASE=mysql+pymysql://[user]:[password]@db:3306/[database_name]'
ADMINISTRATORS=
DEFAULT_USERNAME=
DEFAULT_PASSWORD=
```

```sh
# Comando para subir todos os serviços
$ docker compose up
```

```sh
# Comando para subir todos os serviços em background
$ docker compose up -d
```

### Como acessar o serviço

#### Usuário padrão
| username  |  password |
| :-------: | :-------: |
| admin     | 123       |


| Descrição |  Endereço             |
| :-------: | :-------------------: |
| App 1     | [Link 1](http://localhost:8080) |
| App 2     | [Link 2](http://localhost:8081) |

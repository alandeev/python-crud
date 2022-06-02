# Gerenciamento de tarefas ( Python )

## Descrição

API para controle de tarefas com sistema de login por usuário 

## Ferramentas utilizadas

- Flask
- SQLite ( db local )

## Como instalar?

```bash
1. sudo
2. pip install -r requirements.txt # install pythom modules
3. flask run --host=0.0.0.0 --port=80 # execute server
```


# Rotas 

> Documentação para testes :D
## Autenticação

**Criar usuário**

> [ POST ] http://BASE_URL/users

-> Exemplo de body
```json
{
  "username": "alandev"
}
```

**Editar usuário**

> [ PUT ] http://BASE_URL/users/{user_id}

-> Exemplo de body
```json
{
	"username": "new_username"
}
```

**Deletar usuário**

> [ DELETE ] http://BASE_URL/users/{user_id}

**Listar usuários**

> [ GET ] http://BASE_URL/users

**Consultar usuário especifico**
> [ GET ] http://BASE_URL/users/{user_id}

Passos para instalação:

1 - Instalar as dependências:
```pip install -r requirements.txt```

2 - Edite o conteúdo do arquivo jea/configs/configs.

3 - Gere um ```.env``` local
```python contrib/env_gen.py```

4 - Sincronize a base de dados:
``` python manage.py migrate ```

5 - Crie um superuser:
``` python manage.py createsuperuser```

6 - Teste a aplicação rodando o seguinte comando:
````python manage.py runserver```
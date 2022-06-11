# ProjetoSQL-Fase2
Para iniciar o projeto, primeiramente devemos instalar as dependências, que pode ser feito dando pip install no arquivo `requirements.txt` com o seguinte comando:
```py
pip install -r requirements.txt
```

Logo em seguida deve ser criado o banco de dados. Para isso, foram criados dois scripts: `create_db.sql` e `populate_db.sql`, os quais devem ser executados na plataforma de preferência, como a utilizada pelo grupo: **MySQL Workbench**.

Após isso, é necessário criar um arquivo chamado ".env" na raiz do projeto. Esse arquivo irá conter as credenciais de entrada para o seu banco de dados, ela deve conter a seguinte estrutura (sem espaço entre o "="):
```
USER="USUARIO DO BANCO"
PASSWORD="SENHA DO BANCO"
```
Por fim, rote a programa com:
```
python -m uvicorn main:app --reload
```
Acesse  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para fazer o teste da aplicação!


# Docker
docker build -t leonardodma/fastapi-image .
docker run --name mycontainer -p 127.0.0.1:8000:80 leonardodma/fastapi-image
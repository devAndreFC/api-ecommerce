# DESCRIÇÃO DO PROJETO
Projeto de uma API para gestão de categorias e produtos.
O sistema permite a inclusão, consulta, atualização e exclusão de produtos.
Apenas usuários autenticados podem fazer modificações nos produtos e categorias.
A API permite a consulta de produtos por diferentes parâmetros como nome, descrição e categoria.


# COMO UTILIZAR
Após instalar as tecnologias lstadas na sessão abaixo, execute os comandos na sua IDE(S.O Windows):
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Recomenda-se o uso de um software para testes de API, como o Insonmia;
mas também é possível realizar o cadastro na sessão admin do django, no endereço:
http://127.0.0.1:8000/admin/


# ENDPOINTS
Para acessar todos os produtos: 
http://127.0.0.1:8000/api/v1/produtos/
Se você estiver autenticado, terá a opção para criar um novo produto.

Para acessar um produto específico: 
http://127.0.0.1:8000/api/v1/produtos/ID_DO_PRODUTO
Se você estiver autenticado, terá a opção para editar ou excluir o produto.

Para acessar todas as categorias: 
http://127.0.0.1:8000/api/v1/categorias/
Se você estiver autenticado, terá a opção para criar uma nova categoria.

Para acessar uma categoria específica: 
http://127.0.0.1:8000/api/v1/categorias/ID_DA_CATEGORIA
Se você estiver autenticado, terá a opção para editar ou excluir a categoria.

Para acessar todos os produtos de uma categoria: 
http://127.0.0.1:8000/api/v1/categorias/ID_DA_CATEGORIA/produtos/

Acesse e adicione seu login para criar o seu Token JWT:
http://127.0.0.1:8000/token/
O refresh tem duração de 1 dia. Com ele voce pode redefinir seu token access.

http://127.0.0.1:8000/token/refresh/
O access tem duração de 5 min. Voce precisa informá-lo para fazer modificações nas categorias e produtos.
Com o JTW "access" em mãos é possível adicionar, modificar e excluir categorias e produtos.


# TECNOLOGIAS USADAS
Django para a criação do sistema e DRF para API.
A API utiliza autenticação via Token JWT.
Banco de dados PostgreSQL.


# Lista de todos os recursos usados:
asgiref==3.7.2
certifi==2023.5.7
charset-normalizer==3.2.0
colorama==0.4.6
Django==4.2.3
django-filter==23.2
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
idna==3.4
iniconfig==2.0.0
Markdown==3.4.3
packaging==23.1
Pillow==10.0.0
pluggy==1.2.0
psycopg2==2.9.6
psycopg2-binary==2.9.6
PyJWT==2.7.0
pytest==7.4.0
pytz==2023.3
requests==2.31.0
sqlparse==0.4.4
tzdata==2023.3
urllib3==2.0.3

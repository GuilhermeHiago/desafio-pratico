# desafio-pratico
Django Rest API implementada utilizando Django REST framework

## 🚀 Começando
Basta clonar o repositório e instalar os softwares listados em pré-requisitos

### 📋 Pré-requisitos
* [Python](https://www.python.org/) ou alguma plataforma Python, como o [Anaconda 4.11.0](https://www.anaconda.com/)
#### Python libs
* [Django](https://www.djangoproject.com/)
* [openpyxl](https://www.djangoproject.com/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
* [Django Rest Framework](https://www.django-rest-framework.org)

Observação: Para o projeto Django é recomendado criar um ambiente virtual, neste projeto foi criado com anaconda.

### ⚙️ Run
Ao iniciar o projeto vai estar rodando na porta http://127.0.0.1:8000/. Para rodar o projeto basta rodar o comando:
```
python manage.py runserver
```

📦 Detalhes do Projeto

A API implementada simula um sistema de pedidos, onde:
* Para realizar um pedido o usuário precisa estar cadastrado.
* Um usuário não administrador só tem acesso aos seus próprios pedidos.
* Um usuário pode ver, adicionar, alterar e deletar seus pedidos.

* O usuário deve fornecer nome e data de nascimento para realizar cadastro.
* A senha é opcional, no caso de ausência uma aleatório será atribuída.
* O admin pode consultar os usuários cadastrados, e baixar a lista como xlsx (arquivo de planilha).

## 🛠️ Construído com
* [Anaconda 4.11.0](https://www.anaconda.com/)

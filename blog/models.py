from django.contrib.auth.models import User
from django.db import models

# vamos criar uma tabela no nosso banco de dados para armasenar post


class Post(models.Model):
    title = models.CharField(max_length=255)
    # criando um titulo charfield indica que esse campo tem que receber instrig ate 255 caracteris
    slug = models.SlugField(max_length=255, unique=True)
    # é textoque vamos usar nas nosas url do nosso post
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # vamos criar um campo do autor dos post/
    # on_delete=moldes.cascade significa que quando o autor for deletado as publicaçoes tb sao
    boby = models.TextField()
    # nossos autores podem escrever quanto quiser
    created = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True => significa que ele vai passar a data e a hora q post foi criado
    updated = models.DateTimeField(auto_now=True)
    # mostrar a data de atualizaçaodo post

    def _str_(self):
        return self.title

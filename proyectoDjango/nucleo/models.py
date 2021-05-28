from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='id de la categoria')
    nom_cat = models.CharField(max_length=50, verbose_name='nombre de la categoria')

    def __str__(self):
        return self.nom_cat

class Marca(models.Model):
    id_marca = models.IntegerField(primary_key=True, verbose_name='id de la marca')
    nom_mar = models.CharField(max_length=50,verbose_name='nombre de la marca')

    def __str__(self):
        return self.nom_mar

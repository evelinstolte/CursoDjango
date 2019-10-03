from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField (max_length = 150 , blank = False , null = False)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Autores"

class Livro(models.Model):
    CATEGORIA_CHOICES = (
    (1,'Terror'),
    (2, 'Fantasia'),
    (3,'Suspense'),
)
    categoria = models.IntegerField (choices=CATEGORIA_CHOICES)
    titulo = models.CharField (max_length = 150 , blank = False , null = False)
    isbn = models.PositiveIntegerField()
    autor = models.ForeignKey (Autor , related_name= 'autor' , on_delete = models.PROTECT)
    data = models.DateField(max_length = 150 , blank = True , null = True)
    
    
    def __str__(self):
        return self.titulo + ' - ' + self.autor.nome
    

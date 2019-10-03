from django.contrib import admin
from livros.models import Autor, Livro


class AdminAutor(admin.ModelAdmin):
    list_display = ( 'nome',)
    list_filter = ( 'nome',)
    search_fields = ['nome']

admin.site.register(Autor, AdminAutor)
    
class AdminLivro(admin.ModelAdmin):
    list_display = ( 'titulo',)
    list_filter = ( 'titulo', 'autor','categoria')
    search_fields = ['titulo', 'autor__nome',]

admin.site.register(Livro, AdminLivro)

admin.site.site_header = "Coleção"
admin.site.index_title = 'INFO'
admin.site.site_title = '102'
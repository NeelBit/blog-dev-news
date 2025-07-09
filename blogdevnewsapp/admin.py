from django.contrib import admin
from .models import Usuario, Categoria, Post, Comentario

class UsuarioAdmin(admin.ModelAdmin):
    """ Custom admin interface for Autor model """
    #fields = ('id_autor', 'user', 'nombre', 'email', 'biografia')
    list_display = ('id_autor', 'nombre', 'email', 'biografia')
    search_fields = ('nombre', 'email')
    list_filter = ('email','nombre')

# Register your models here.
admin.site.site_header = "Panel de Administración de MyBlog"
admin.site.site_title = "MyBlog Admin"
admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Comentario)

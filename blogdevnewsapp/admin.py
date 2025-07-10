from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Categoria, Post, Comentario, Etiqueta

class UsuarioAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'fecha_registro')
    search_fields = ('username', 'email')
    list_filter = ('fecha_registro',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('nombre',)

class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    list_filter = ('nombre',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'contenido', 'categoria', 'fecha_publicacion', 'imagen', 'slug')
    search_fields = ('titulo', 'autor__username')
    list_filter = ('categoria', 'autor')
    filter_horizontal = ('etiquetas',)  # Esto agrega un widget para seleccionar varias etiquetas

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'autor', 'fecha_publicacion', 'activo')
    search_fields = ('post__titulo', 'autor__username', 'contenido')
    list_filter = ('activo', 'fecha_publicacion')

admin.site.site_header = "Panel de Administración de Blog Dev News"
admin.site.site_title = "Blog Dev News Admin"

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)

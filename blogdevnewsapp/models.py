from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    #
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100, blank=True, null=True)
    telefono=models.CharField(max_length=15, blank=True, null=True)
    email=models.EmailField(unique=True)
    

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre=models.CharField(max_length=100, unique=True)
    descripcion=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    def agregar_post(self, post):
        post.categoria = self
        post.save()

class Post(models.Model):
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_publicacion=models.DateTimeField(auto_now=True, blank=True, null=True)

    categorias=models.ManyToManyField(Categoria, blank=True, related_name='posts')

    def __str__(self):
        return self.titulo
    
    def publicar_articulo(self):
        self.fecha_publicacion = self.fecha_creacion
        self.save()

class Comentario(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    #autor=models.CharField(max_length=100)
    autor_comentario=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    contenido=models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)

    comentario_padre=models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='respuestas'
    )

    def __str__(self):
        return f'Comentario de {self.autor_comentario} en {self.post.titulo} - {self.contenido[:20]}...'
    
    def publicar_comentario(self):
        self.save()


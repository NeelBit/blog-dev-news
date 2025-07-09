from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# https://docs.djangoproject.com/es/5.2/topics/auth/customizing/
# https://codigofacilito.com/articulos/django-user-model
class Usuario(AbstractUser):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    # https://www.desarrollolibre.net/blog/django/upload-o-carga-de-archivos-en-django-avatar
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)

    def __str__(self):
        return self.username

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    """ def agregar_post(self, post):
        post.categoria = self
        post.save() """

class Post(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    # Solamente puede tener una categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    """ # Puede tener varias etiquetas
    etiquetas = models.ManyToManyField('Etiqueta', blank=True, related_name='posts') """
    # Para generar un slug único basado en el título (direccion url amigable)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    """ def publicar_articulo(self):
        self.fecha_publicacion = self.fecha_creacion
        self.save() """
    
    # Generar automaticamente el slug a partir del título, sobreescribiendo el save
    def save(self, *args, **kwargs):
        if not self.slug and self.titulo:
            from django.utils.text import slugify
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    # para posible moderación de comentarios
    activo = models.BooleanField(default=True)

    comentario_padre=models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='respuestas'
    )

    def __str__(self):
        return f'Comentario de {self.autor} en {self.post.titulo} - {self.contenido[:20]}...'
    
    """ def publicar_comentario(self):
        self.save() """

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.nombre
    
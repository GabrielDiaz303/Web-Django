from django.db import models

# Create your models here.
class Mascota(models.Model):
    title = models.CharField(max_length=50,verbose_name = "Título")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "mascotas")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificación")
    
    def __str__(self) -> str:
        return self.title
    
    


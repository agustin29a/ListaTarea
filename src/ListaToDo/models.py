from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Lista(models.Model):
    
    STATE_CHOICES = (
        ('A', 'Todo'),
        ('B', 'In Progress'),
        ('C', 'Done'),
        ('D', 'Close'),
    )
     
    name = models.CharField('Nombre', max_length=30)
    description = models.CharField('Descripcion', max_length=200)
    state = models.CharField('Estado', max_length=4, choices=STATE_CHOICES, default='A')
    date_expire = models.DateTimeField('Fecha Vencimiento', null=True, blank=True)
    coment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField( auto_now_add=True )
    last_update = models.DateTimeField( auto_now=True )

    def get_absolute_url(self):
        return reverse('list')     
    
    def __str__(self):
        return f'{self.name.title()}, {self.description.title()}'

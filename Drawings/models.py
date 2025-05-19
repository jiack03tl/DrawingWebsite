from django.db import models
from django.utils import timezone
# Create your models here.
class AllDrawing(models.Model):
    DRAWING_TYLE_CHOICES = [
        ('Pencil', 'Pencil'),
        ('Charcoal', 'Charcoal'),
        ('Watercolor', 'Watercolor'),
        ('Oil', 'Oil'),
        ('Acrylic', 'Acrylic'),
        ('Digital', 'Digital'),
        ('Mixed Media', 'Mixed Media'),
        ('Soft-Pastels', 'Soft-Pastels'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Drawings/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=50, choices=DRAWING_TYLE_CHOICES)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.description
    

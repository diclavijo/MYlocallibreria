from django.db import models
from django.urls import reverse 
import uuid 


# Create your models here.
class Genre(models.Model):

	name = models.CharField(max_length=100)
	

	class Meta:
		ordering = ['name']

	def get_absolute_url(self):
		return reverse('genre-detail', args=[str(self.id)])

	def __str__(self):
		
		return self.name

class Alimento(models.Model):
    
	title = models.CharField(max_length=200)

	producto = models.ForeignKey('producto', on_delete=models.SET_NULL, null=True)
    
	summary = models.TextField(max_length=1000)
	isbn = models.CharField('ISBN', max_length=13,)
	genre = models.ManyToManyField(Genre)
	imagen = models.ImageField(upload_to='media/', null=True, blank=True)
    
	def __str__(self):
		return self.title
    
	def get_absolute_url(self):
		
		return reverse('alimento-detail', args=[str(self.id)])


class AlimentoInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	alimento = models.ForeignKey('Alimento', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	alimento_disponible = models.DateField(null=True, blank=True)

	DISPONIBILIDAD = (
		('E', 'En_envio'),
		('R', 'Reservado'),
		('D', 'Disponible'),
		('M', 'Mantencion'),
	)


	status = models.CharField(
		max_length=1,
		choices=DISPONIBILIDAD,
		blank=True,
		default='D',
		help_text='Alimento_Disponible',
	)

	class Meta:
		ordering = ['alimento_disponible']


	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.alimento.title})'



class Producto(models.Model):
	
	nombre_producto = models.CharField(max_length=100)	
	fecha_ingreso = models.DateField(null=True, blank=True)
	fecha_caducidad = models.DateField('Caduce', null=True, blank=True)

	class Meta:
		ordering = ['nombre_producto']

	def get_absolute_url(self):
		return reverse('producto-detail', args=[str(self.id)])
		

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.nombre_producto}'	
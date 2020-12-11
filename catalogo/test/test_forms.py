from django.test import TestCase
from catalogo.forms import ProductoForm, AlimentoForm
from catalogo.models import Producto, Alimento
from django.core.files.uploadedfile import SimpleUploadedFile

class ProductoFormsTest(TestCase):
    def test_valid_form(self):
        g = Genre.objects.create(name='Prueba1', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GenreForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Genre.objects.create(name='', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GenreForm(data=data)
        self.assertFalse(form.is_valid())

class AlimentoFormsTest(TestCase):
    def test_valid_form(self):
        genre = Genre.objects.create(name='razaPequeña', summary='Prueba')
        genre = Genre.objects.get(pk=1).pk
        a = alimento.objects.create(title='Prueba1', summary='Prueba')
        a.save()
        data = {'title': a.title, 'summary': a.summary, 'genre': genre, }
        
        form = AlimentoForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Genre.objects.create(name='Accion', summary='Prueba')
        a = Alimento.objects.create(title='', summary='Prueba', genre=g, )
        data = {'title': a.title, 'summary': a.summary, 'genre': a.genre, }
        form = AlimentoForm(data=data)
        self.assertFalse(form.is_valid())
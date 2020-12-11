from django.test import TestCase
from catalogo.models import Producto, Alimento
      
class ProductoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Producto.objects.create(Nombre_producto='CarChow')

    def test_nombre_producto_label(self):
        producto=Producto.objects.get(id=1)
        field_label = producto._meta.get_field('nombre_producto').verbose_name
        self.assertEquals(field_label,'nombre_producto')

    def test_fecha_caducidad_label(self):
        producto=Producto.objects.get(id=1)
        field_label = producto._meta.get_field('fecha_caducidad').verbose_name
        self.assertEquals(field_label,'died')

    def test_nombre_producto_max_length(self):
        producto=Producto.objects.get(id=1)
        max_length = producto._meta.get_field('nombre_producto').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        producto=Producto.objects.get(id=1)
        expected_object_name = '%s, %s' % (producto.nombre_producto)
        self.assertEquals(expected_object_name,str(producto))

    def test_get_absolute_url(self):
        producto=Producto.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(producto.get_absolute_url(),'/catalogo/producto/1')


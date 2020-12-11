from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from catalogo.models import Producto

from django.test import TestCase

# Create your tests here.

class ProductoListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_productos = 13
        for producto_num in range(number_of_productos):
            Producto.objects.create(nombre_producto='Diego %s' % producto_num, % producto_num,)
           
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/catalogo/productos/') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('productos'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('productos'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalogo/alimento_list.html')
        
    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('productos'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['alimento_list']) == 10)

    def test_lists_all_productos(self):
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('productos')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['alimento_list']) == 3)
from django import forms
from . models import Producto


class ProductoForm(forms.ModelForm):
    nombre_producto = forms.CharField(label='Nombre',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    summary = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    fecha_ingreso = forms.DateField(label='Ingreso', max_length=100,widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    fecha_caducidad = forms.DateField(label='Caducidad', max_length=100,widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = Producto
        fields = ('nombre_producto','summary','fecha_ingreso', 'fecha_caducidad')

        
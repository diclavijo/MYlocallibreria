from django.shortcuts import render
from .models import Alimento, Producto, AlimentoInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_alimentos=Alimento.objects.all().count()
    num_instances=AlimentoInstance.objects.all().count()
    # Libros disponibles (status = 'a')
  

    num_visits=request.session.get('num_visits', 0)
    num_visits=request.session['num_visits']=num_visits+1
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_alimentos':num_alimentos,'num_instances':num_instances},
    )

def galeria(request):
    return render(
        request,
        'galeria.html',
    )    
def formulario(request):
    return render(
        request,
        'formulario.html',
    )   


class AlimentoListView(generic.ListView):
    model = Alimento
    paginate_by = 10
class AlimentoDetailView(generic.DetailView):
    model = Alimento




from django.views import generic

class ProductoDetailView(generic.DetailView):

    model = Producto


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto

class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
    initial={'fecha_caducidad':'05/01/2022',}

class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['nombre_producto','fecha_ingreso','fecha_caducidad']

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')

from .forms import RenewAlimentoForm
from catalogo.forms import RenewAlimentoForm



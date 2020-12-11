from django.shortcuts import render
from .models import Alimento, Producto, AlimentoInstance, Genre
from django.views import generic

# Create your views here.
def index(request):

    num_alimentos=Alimento.objects.all().count()
    num_instances=AlimentoInstance.objects.all().count()


    num_visits=request.session.get('num_visits', 0)
    num_visits=request.session['num_visits']=num_visits+1

    return render(
        request,
        'index.html',
        context={'num_alimentos':num_alimentos,'num_instances':num_instances,'num_visits':num_visits},
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
from django.contrib.auth.forms import UserCreationForm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
    initial={'fecha_caducidad':'05/01/2022'}

class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['nombre_producto','fecha_ingreso','fecha_caducidad']

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')





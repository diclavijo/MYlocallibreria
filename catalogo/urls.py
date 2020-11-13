from django.urls import path 
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('formulario/', views.formulario, name='formulario'),
	path('galeria/', views.galeria, name='galeria'),
	path('producto/<int:pk>', views.ProductoDetailView.as_view(), name='producto-detail'),
	path('',views.index,name='index'),
	path('alimentos/', views.AlimentoListView.as_view(), name='alimentos'),
    path('alimento/<int:pk>', views.AlimentoDetailView.as_view(), name='alimento-detail'),
]



urlpatterns += [
    path('producto/create/', views.ProductoCreate.as_view(), name='producto_create'),
    path('producto/<int:pk>/update/', views.ProductoUpdate.as_view(), name='producto_update'),
    path('producto/<int:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),

]


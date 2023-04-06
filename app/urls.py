from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_form,name='producto_insert'), # get y post req. para  insert 
    path('<int:id>/', views.producto_form,name='producto_update'), # get y post req. para update
    path('delete/<int:id>/',views.producto_delete,name='producto_delete'), # para eliminar
    path('list/',views.producto_list,name='producto_list') # get req. para recuparar y listar todos los registros
]
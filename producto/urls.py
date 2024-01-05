from django.contrib import admin
from django.urls import path, include
from .views import Producto_form,Producto_view,Producto_edit,ProductoQueryView

app_name="producto"
urlpatterns = [
	path('add_producto/', Producto_form,name="Producto_form"),
    path('view_producto/', Producto_view,name="Producto_view"),
    path('edit_producto/<int:myID>/', Producto_edit,name='Producto_edit'),
    path('query/',ProductoQueryView.as_view(),name='producto-query')
]

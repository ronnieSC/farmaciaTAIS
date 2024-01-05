"""farmacia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import Proveedor_form,Proveedor_view,Proveedor_edit

app_name="proveedor"
urlpatterns = [
	path('add_proveedor/', Proveedor_form,name="Proveedor_form"),
    path('view_proveedor/', Proveedor_view,name="Proveedor_view"),
    path('edit_proveedor/<int:myID>/', Proveedor_edit,name='Proveedor_edit'),
]

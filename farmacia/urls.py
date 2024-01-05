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
from home.views import Sticky_form,Sticky_view,Testimonial_form,register,login,change_password,logout,delete,Testimonial_view

urlpatterns = [
    path('', include('home.urls')),
    path('shop/', include('shop.urls')),
    path('admin/', admin.site.urls),
    path('sticky_add',Sticky_form,name='sticky'),
    path('sticky_view',Sticky_view,name='sticky_view'),
    path('testimonial_add',Testimonial_form,name='testimonial'),
    path('testimonial_view',Testimonial_view,name='testimonial_view'),
    path('add_user',register,name='register'),
    path('login',login,name='login'),
    path('delete',delete,name='delete'),
    path('change_password',change_password,name='change_password'),
    path('logout',logout,name='logout'),
    path('proveedor/', include('proveedor.urls')),
    path('producto/', include('producto.urls')),
    path('cliente/', include('cliente.urls')),
    path('ventas/', include('venta.urls')),
]

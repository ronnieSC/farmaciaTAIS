from django import forms

from .models import Producto
from proveedor.models import Proveedor

class ProductoForm(forms.ModelForm):

    class Meta:
        model=Producto
        fields=[
            'nombre',
            'descripcion',
            'proveedor',
            'precio',
            'cantidad',
            'oferta',
            'imagen',]
            
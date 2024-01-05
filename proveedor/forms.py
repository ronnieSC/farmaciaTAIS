from django import forms
import datetime
from .models import Proveedor

class ProveedorForm(forms.Form):
    razonsocial=forms.CharField(max_length=300)
    direccion=forms.CharField(max_length=300)
    email=forms.EmailField(max_length=300)
    telefono=forms.IntegerField()
    representante=forms.CharField(max_length=300)
    fechacontratacion= forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Seleccione Año", "Seleccione Mes", "Seleccione Dia"), years=range(1980,  datetime.date.today().year+1)
    ),
)

    

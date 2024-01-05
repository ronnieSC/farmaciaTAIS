from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
import datetime
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,View)
from .models import Cliente
from django.http import JsonResponse,HttpResponse
# Create your views here.
class ClienteListView(ListView):
    model = Cliente

class ClienteDetailView(DetailView):
    model = Cliente

class ClienteCreateView(CreateView):
    model=Cliente
    fields=[
        'nombres',
        'apellidos',
        'direccion',
        'DNI',
        'edad',
        'email',
        'telefono',
        'fechainicio'
        ]
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['fechainicio'].widget = forms.SelectDateWidget(
        empty_label=("Seleccione Año", "Seleccione Mes", "Seleccione Dia"), years=range(1980,  datetime.date.today().year+1)
    )
        return form

class CustomForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields=[
            'nombres',
            'apellidos',
            'direccion',
            'DNI',
            'edad',
            'email',
            'telefono',
            'fechainicio'
            ]
        widgets = {
            'fechainicio': forms.SelectDateWidget(
        empty_label=("Seleccione Año", "Seleccione Mes", "Seleccione Dia"), years=range(1980,  datetime.date.today().year+1)
        )
        }

class ClienteUpdateView(UpdateView):
    form_class = CustomForm
    model=Cliente

class ClienteDeleteView(DeleteView): 
    model= Cliente
    success_url=reverse_lazy('cliente:cliente-list')

class ClienteQueryView(View):
    def get(self,request,*args,**kwargs):
        queryset=Cliente.objects.all()
        if request.user.is_authenticated==True:
            return JsonResponse(list(queryset.values()),safe=False)
        else:
            return HttpResponse('')


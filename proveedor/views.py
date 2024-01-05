from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.forms.models import model_to_dict
from django.contrib import messages
from .models import Proveedor
from django import forms
from .models import Proveedor
from .forms import ProveedorForm

def Proveedor_form(request):
	form=ProveedorForm()
	if request.method == 'POST':
		form=ProveedorForm(request.POST)
		if form.is_valid():
			Proveedor.objects.create(**form.cleaned_data)
			form=ProveedorForm()
			messages.info(request,'Item Añadido con Exito')
	#else:
		#messages.info(request,'Error')
	context={
		'form':form
		}
	return render(request,'proveedor/proveedor_form.htm',context)

def Proveedor_view(request):
	if request.method=='POST':
		checked = request.POST.getlist('CHECKED')
		for ch in checked:
			obj=get_object_or_404(Proveedor, id=ch)
			obj.delete()
	proveedor=Proveedor.objects.all()
	context={
		'proveedor':proveedor,
		}
	return render(request,'proveedor/proveedor_view.htm',context)

def Proveedor_edit(request,myID):
	if request.method == 'POST':
		obj=get_object_or_404(Proveedor, id=myID)
		form=ProveedorForm(request.POST, request.FILES or None)
		if form.is_valid():
			Proveedor.objects.filter(id=myID).update(**form.cleaned_data)
			form=ProveedorForm()
			#messages.info(request,'Item Editado con Exito')
			return redirect('../../view_proveedor')
	else:
		obj=get_object_or_404(Proveedor, id=myID)
		initialvalues =obj.__dict__
		form=ProveedorForm(None,initial=initialvalues)
	
	context={
		'form':form
		}
	return render(request,'proveedor/proveedor_edit.htm',context)

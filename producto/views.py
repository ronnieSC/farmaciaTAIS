from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User, auth
from django.forms.models import model_to_dict
from django.contrib import messages
from .forms import ProductoForm
from .models import Producto
from django.views.generic import (View)

# Create your views here.
def Producto_form(request):
	if request.method == 'POST':
		form=ProductoForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			form=ProductoForm()
			#messages.info(request,'Item Añadido con Exito')
	else:
		form = ProductoForm()
	
	context={
		'form':form
		}
	return render(request,'producto/product_form.htm',context)

def Producto_view(request):
	if request.method=='POST':
		checked = request.POST.getlist('CHECKED')
		for ch in checked:
			obj=get_object_or_404(Producto, id=ch)
			obj.delete()
	producto=Producto.objects.all()
	context={
		'productos':producto,
		}
	return render(request,'producto/product_view.htm',context)    

def Producto_edit(request,myID):
	if request.method == 'POST':
		obj=get_object_or_404(Producto, id=myID)
		form=ProductoForm(request.POST, request.FILES or None,instance=obj)
		if form.is_valid():
			form.save()
			#messages.info(request,'Item Editado con Exito')
			return redirect('../../view_producto')
	else:
		obj=get_object_or_404(Producto, id=myID)
		form = ProductoForm(instance=obj)
	
	context={
		'form':form
		}
	return render(request,'producto/product_edit.htm',context)


class ProductoQueryView(View):
	def get(self,request,*args,**kwargs):
		queryset=Producto.objects.all()
		if request.user.is_authenticated==True:
			return JsonResponse(list(queryset.values()),safe=False)
		else:
			return HttpResponse('')



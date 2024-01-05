from django.shortcuts import render,redirect, get_object_or_404
from producto.models import Producto
from django.http import HttpResponse
from cliente.models import Cliente
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Venta
from datetime import date,datetime
from .utils import render_to_pdf
from django.views.generic import (View)
from django.core.mail import send_mail

# Create your views here.
def Venta_form(request):
	if request.method=='POST':
		if (verify_fields(request=request)==False):
			messages.info(request,'Error en los datos ingresados')
			return render(request,'venta/venta_form.htm',{}) 
		if (verify_existences(request=request)==False):
			messages.info(request,'Existencias agotadas o valores repetidos en la lista')
			return render(request,'venta/venta_form.htm',{}) 
		i=0
		detalles="<tr>\n<th>Nombre</th><th>Descripción</th><th>Cantidad</th><th>Precio</th>\n</tr>\n"
		cliente=get_object_or_404(Cliente, id=request.POST.getlist('cliente')[0])
		vendedor=get_object_or_404(User, id=request.user.id)
		prod_id = request.POST.getlist('txtprecio')
		for ch in prod_id:
			producto=get_object_or_404(Producto, id=request.POST.getlist('cboxproducto')[i])
			detalles+="<tr>\n"
			detalles+="<td>"+producto.nombre+"</td>"+"<td>"+request.POST.getlist('txtdescripcion')[i]+"</td>"
			detalles+="<td>"+request.POST.getlist('cboxcantidad')[i]+"</td>"+"<td>"+request.POST.getlist('txtprecio')[i]+"</td>\n"
			detalles+="</tr>\n"
			i+=1
		total=request.POST.getlist('total')[0]
		today = datetime.now()
		fecha=today
		i=0
		pid = request.POST.getlist('cboxproducto')
		for ch in pid:
			obj=get_object_or_404(Producto, id=ch)
			Producto.objects.filter(id=ch).update(cantidad=int(obj.cantidad)-int(request.POST.getlist('cboxcantidad')[i]))
			i+=1
		venta=Venta(cliente=cliente, vendedor=vendedor, detalles=detalles, total=total, fecha=fecha)
		venta.save()
		messages.info(request,'Item Añadido con Exito')
	return render(request,'venta/venta_form.htm',{})  

def Venta_view(request):
	if request.method=='POST':
		checked = request.POST.getlist('CHECKED')
		for ch in checked:
			obj=get_object_or_404(Venta, id=ch)
			obj.delete()
	venta=Venta.objects.all()
	context={
		'ventas':venta,
		}
	return render(request,'venta/ventas_hechas.htm',context)

def Venta_details(request,myID):
	obj=get_object_or_404(Venta, id=myID)
	
	context={
		'form':obj
		}
	return render(request,'venta/detalle_venta.htm',context)

def verify_fields(request):
	client_fields = ["cliente", "DNI", "txtdireccion","txtemail","txttelefono"]
	for x in client_fields:
		if (request.POST.getlist(x)[0]==""):
			return False
	i=0
	pre = request.POST.getlist('txtprecio')
	for ch in pre:
		if (request.POST.getlist('cboxproducto')[i]=="" or request.POST.getlist('cboxproducto')[i]=="0"):
			return False
		if (request.POST.getlist('txtdescripcion')[i]=="" or request.POST.getlist('txtdescripcion')[i]=="0" ):
			return False
		if (request.POST.getlist('cboxcantidad')[i]=="" or request.POST.getlist('cboxcantidad')[i]=="0" ):
			return False
		if (request.POST.getlist('txtprecio')[i]=="" or request.POST.getlist('txtprecio')[i]=="0" ):
			return False
		i+=1
	return True

def verify_existences(request):
	i=0
	prod_id = request.POST.getlist('cboxproducto')
	if (len(prod_id) != len(set(prod_id))):
		return False
	for ch in prod_id:
		obj=get_object_or_404(Producto, id=ch)
		if (int(obj.cantidad)-int(request.POST.getlist('cboxcantidad')[i])<0):
			return False
		i+=0
	return True

def GeneratePdf(request,myID):
	obj=get_object_or_404(Venta, id=myID)
	context={
		'form':obj
	}
	pdf = render_to_pdf('venta/detalle_venta_pdf.htm', context)
	return HttpResponse(pdf, content_type='application/pdf')

def Givemail(request,myID):
	if request.user.is_authenticated:
		obj=get_object_or_404(Venta, id=myID)
		context={
			'form':obj
		}
		send_mail('Hola de myPharmia',
		'Hola, te estamos enviando la factura correspondiente a la compra que hiciste:\n'+request.build_absolute_uri() +"../download_pdf/\nAtentamente",
		'mypharmiaempresa@gmail.com',
		[obj.cliente.email],
		fail_silently=False)
		messages.info(request,'Mensaje enviado a '+obj.cliente.email)
	return redirect('../../../ver_formularios/')

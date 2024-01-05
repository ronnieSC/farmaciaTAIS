from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Sticky,Testimonial

# Create your views here.
def myHomeView(request,*args,**kwargs):
	myContext={
	'Sticky': Sticky.objects.all(),
	'Testimonials': Testimonial.objects.all(),
	}
	return render(request,"home/index.html",myContext)

def Sticky_form(request):
	if request.method=='POST':
		titulo=request.POST['txttitulo']
		subtitulo=request.POST['txtsubtitulo']
		cuerpo=request.POST['txtcuerpo']
		color=request.POST['cboxcolor']
		sticky=Sticky(titulo=titulo, subtitulo=subtitulo, descripcion=cuerpo, color=color)
		sticky.save()
		messages.info(request,'Item Añadido con Exito')
		return redirect('/')
	else:
		return render(request,'home/sticky_form.htm',{})

def Sticky_view(request):
	if request.method=='POST':
		checked = request.POST.getlist('CHECKED')
		for ch in checked:
			obj=get_object_or_404(Sticky, id=ch)
			obj.delete()
	sticky=Sticky.objects.all()
	context={
		'stickys':sticky,
		}
	return render(request,'home/sticky_view.htm',context)    

def Testimonial_form(request):
	if request.method=='POST':
		nombre=request.POST['txtnombre']
		descripcion=request.POST['txtdescripcion']
		imagen=request.FILES['imageupload']
		sticky=Testimonial(nombre=nombre, descripcion=descripcion, imagen=imagen)
		sticky.save()
		messages.info(request,'Item Añadido con Exito')
		return redirect('/')
	else:
		return render(request,'home/testimonial_form.htm',{})


def Testimonial_view(request):
	if request.method=='POST':
		checked = request.POST.getlist('CHECKED')
		for ch in checked:
			obj=get_object_or_404(Testimonial, id=ch)
			obj.delete()
	testimonial=Testimonial.objects.all()
	context={
		'testimonios':testimonial,
		}
	return render(request,'home/testimonial_view.htm',context)    

def logout(request):
	auth.logout(request)
	return redirect("/")

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect("/")
		else:
			#messages.info(request,'Invalid Credentials')
			return redirect('login')
	else:
		return render(request,'home/login_form.htm',{})


def delete(request):
	if request.method=='POST':
		checked = request.POST.getlist('CHECKED')
		for ch in checked:
			obj=get_object_or_404(User, id=ch)
			obj.delete()
	user=User.objects.all()
	context={
		'usuarios':user,
		}
	return render(request,'home/del_form.html',context) 

def change_password(request):
	if request.method == 'POST':
		opassword = request.POST['opassword']
		npassword = request.POST['npassword']
		npassword2 = request.POST['npassword2']
		if (opassword=="" or npassword=="" or npassword2==""):
			messages.info(request,'Password are empty')
			return redirect('change_password')
		u = User.objects.get(id=request.user.id)
		if u.check_password(opassword):
			if npassword==npassword2:
				u.set_password(npassword)
				u.save()
				return redirect('/')
			else:
				messages.info(request,'Password are different...')
				return redirect('change_password')
		else:
			messages.info(request,'Old password are not the same...')
			return redirect('change_password')
		return redirect('/')
	else:
		return render(request,'home/change_password.htm',{});

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Taken')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save();
				messages.info(request,'User created')
				return redirect('register')
		else:
			messages.info(request,'Password not matching...')
			return redirect('register')
		return redirect('/')
	else:
		return render(request,'home/register_form.htm',{});


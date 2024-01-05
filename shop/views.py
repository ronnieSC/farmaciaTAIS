from django.shortcuts import render
from producto.models import Producto

# Create your views here.
def myShopView(request,*args,**kwargs):
	myContext={
	'Productos': Producto.objects.all(),
	}
	return render(request,"shop/shop.html",myContext)

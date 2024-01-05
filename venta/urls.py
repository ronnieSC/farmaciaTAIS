from django.contrib import admin
from django.urls import path, include
from .views import Venta_form,Venta_view, Venta_details,GeneratePdf,Givemail

app_name="venta"
urlpatterns = [
	path('formulario_venta/', Venta_form,name="Venta_form"),
	path('ver_formularios/', Venta_view,name="Venta_view"),
	path('Venta_details/<int:myID>/', Venta_details,name='Venta_details'),
	path('Venta_details/<int:myID>/download_pdf/',GeneratePdf,name='download-venta'),
	path('Venta_details/<int:myID>/send_email/',Givemail,name='give-email'),
]

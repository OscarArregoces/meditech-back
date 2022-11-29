"""meditech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main.views import *
from main.consulta1 import export_pdf
from main.consulta2 import export_pdf2
from main.consulta3 import export_pdf3
from main.consulta4 import export_pdf4
from main.consulta5 import export_pdf5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('checkusuario/', CheckUsuario.as_view()),
    path('servicioDetail/', ServiciosDetail.as_view()),
    path('updateServicio/<int:pk>/', UpdateServicio.as_view()),
    path('consulta1/', Consulta1.as_view()),
    path('consulta2/', Consulta2.as_view()),
    path('consulta3/', Consulta3.as_view()),
    path('consulta4/', Consulta4.as_view()),
    path('consulta5/', Consulta5.as_view()),
    path('pdf1/', export_pdf),
    path('pdf2/', export_pdf2),
    path('pdf3/', export_pdf3),
    path('pdf4/', export_pdf4),
    path('pdf5/', export_pdf5),
]

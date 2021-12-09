from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio,name='home'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('productos',views.productos,name='productos'),
    path('productos/crear',views.crear,name='crear'),
    path('productos/eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('productos/editar/<int:id>',views.editar,name='editar'),
    path('productosjson',views.productosjson,name='productosjson'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'usuarios'

urlpatterns = [
path('registrar/',views.RegistrarUsuario.as_view(), name='registrar'),
    path('iniciar_sesion/', LoginView.as_view(template_name="usuarios/iniciar_sesion.html"), name='iniciar_sesion'),
    path('cerrar_sesion/', LogoutView.as_view(), name='cerrar_sesion'),
    path('listar_usuarios/', ListarUsuarios, name='listar_usuarios'),
    path("eliminar_usuario/<int:pk>", EliminarUsuario.as_view(), name='eliminar_usuario'),
       

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

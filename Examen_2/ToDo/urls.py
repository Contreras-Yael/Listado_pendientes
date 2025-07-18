# todo/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_lista_pendientes, name='api_lista_pendientes'),
    path('importar/', views.importar_api, name='importar_api'),
    path('crear/', views.crear_pendiente, name='crear_pendiente'),
    path('editar/<int:pk>/', views.editar_pendiente, name='editar_pendiente'),
    path('eliminar/<int:pk>/', views.eliminar_pendiente, name='eliminar_pendiente'),

    path('lista/id/', views.lista_id, name='lista_id'),
    path('lista/id_title/', views.lista_id_title, name='lista_id_title'),
    path('lista/no_resueltos/', views.lista_no_resueltos, name='lista_no_resueltos'),
    path('lista/resueltos/', views.lista_resueltos, name='lista_resueltos'),
    path('lista/id_user/', views.lista_id_user, name='lista_id_user'),
    path('lista/resueltos_user/', views.lista_resueltos_user, name='lista_resueltos_user'),
    path('lista/no_resueltos_user/', views.lista_no_resueltos_user, name='lista_no_resueltos_user'),

    path('api/lista/', views.api_lista_pendientes, name='api_lista_pendientes'),
    path('api/detalle/<int:pk>/', views.api_detalle_pendiente, name='api_detalle_pendiente'),

    path('mis-pendientes/', views.lista_pendientes_local, name='lista_pendientes_local'),
    path('marcar-completado/<int:pk>/', views.marcar_completado, name='marcar_completado'),
    path('marcar-pendiente/<int:pk>/', views.marcar_pendiente, name='marcar_pendiente'),
]
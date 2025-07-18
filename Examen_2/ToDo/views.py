# todo/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Pendiente
from .forms import PendienteForm
import requests
from django.http import JsonResponse  # ya importado si seguiste sugerencias previas
from django.urls import reverse

# Obtener datos del API externo (solo una vez o manualmente)
def importar_api(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    if response.status_code == 200:
        for item in response.json():
            Pendiente.objects.get_or_create(
                id=item['id'],
                defaults={
                    'title': item['title'],
                    'userId': item['userId'],
                    'completed': item['completed']
                }
            )
    return redirect('lista_id_title')

# CRUD
def crear_pendiente(request):
    form = PendienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_id_title')
    return render(request, 'todo/form.html', {'form': form})

def editar_pendiente(request, pk):
    pendiente = get_object_or_404(Pendiente, pk=pk)
    form = PendienteForm(request.POST or None, instance=pendiente)
    if form.is_valid():
        form.save()
        return redirect('lista_id_title')
    return render(request, 'todo/form.html', {'form': form})

def eliminar_pendiente(request, pk):
    pendiente = get_object_or_404(Pendiente, pk=pk)
    if request.method == 'POST':
        pendiente.delete()
        return redirect('lista_id_title')
    return render(request, 'todo/confirmar.html', {'pendiente': pendiente})

# Vistas filtradas
def lista_id(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    pendientes = []
    if response.status_code == 200:
        pendientes = response.json()
    # Solo IDs
    ids = [{'id': p['id']} for p in pendientes]
    return render(request, 'todo/lista_id.html', {'pendientes': ids})

def lista_id_title(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    pendientes = []
    if response.status_code == 200:
        pendientes = response.json()
    # IDs y Titles
    datos = [{'id': p['id'], 'title': p['title']} for p in pendientes]
    return render(request, 'todo/lista_id_title.html', {'pendientes': datos})

def lista_no_resueltos(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    pendientes = []
    if response.status_code == 200:
        pendientes = response.json()
    # Solo pendientes no resueltos (ID y Title)
    datos = [{'id': p['id'], 'title': p['title']} for p in pendientes if not p['completed']]
    return render(request, 'todo/lista_no_resueltos.html', {'pendientes': datos})

def lista_resueltos(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    pendientes = []
    if response.status_code == 200:
        pendientes = response.json()
    # Solo pendientes resueltos (ID y Title)
    datos = [{'id': p['id'], 'title': p['title']} for p in pendientes if p['completed']]
    return render(request, 'todo/lista_resueltos.html', {'pendientes': datos})

def lista_id_user(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    pendientes = []
    if response.status_code == 200:
        pendientes = response.json()
    # IDs y userID
    datos = [{'id': p['id'], 'userId': p['userId']} for p in pendientes]
    return render(request, 'todo/lista_id_user.html', {'pendientes': datos})

def lista_resueltos_user(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    pendientes = []
    if response.status_code == 200:
        pendientes = response.json()
    # Resueltos (ID y userID)
    datos = [{'id': p['id'], 'userId': p['userId']} for p in pendientes if p['completed']]
    return render(request, 'todo/lista_resueltos_user.html', {'pendientes': datos})

def lista_no_resueltos_user(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    pendientes = []
    if response.status_code == 200:
        pendientes = response.json()
    # No resueltos (ID y userID)
    datos = [{'id': p['id'], 'userId': p['userId']} for p in pendientes if not p['completed']]
    return render(request, 'todo/lista_no_resueltos_user.html', {'pendientes': datos})

def api_lista_pendientes(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    pendientes = []
    if response.status_code == 200:
        pendientes = response.json()
    return render(request, 'todo/api_lista.html', {'pendientes': pendientes})

def api_detalle_pendiente(request, pk):
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{pk}')
    pendiente = None
    if response.status_code == 200:
        pendiente = response.json()
    return render(request, 'todo/api_detalle.html', {'pendiente': pendiente})

# Vista principal para pendientes locales
def lista_pendientes_local(request):
    pendientes = Pendiente.objects.all()
    return render(request, 'todo/lista.html', {'pendientes': pendientes})

# Cambiar estado a completado
def marcar_completado(request, pk):
    pendiente = get_object_or_404(Pendiente, pk=pk)
    pendiente.completed = True
    pendiente.save()
    return redirect('lista_pendientes_local')

# Cambiar estado a pendiente
def marcar_pendiente(request, pk):
    pendiente = get_object_or_404(Pendiente, pk=pk)
    pendiente.completed = False
    pendiente.save()
    return redirect('lista_pendientes_local')


from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def inicio(request):
    return render(request, "tienda/inicio.html")

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "tienda/lista_clientes.html", {"clientes": clientes})

def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_clientes")
    else:
        form = ClienteForm()
    return render(request, "tienda/form_cliente.html", {"form": form})

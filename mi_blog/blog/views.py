from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm
from .models import Post

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_post')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

def buscar_post(request):
    resultados = []
    if request.method == 'GET':
        form = BusquedaPostForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaPostForm()
    return render(request, 'blog/buscar_post.html', {'form': form, 'resultados': resultados})

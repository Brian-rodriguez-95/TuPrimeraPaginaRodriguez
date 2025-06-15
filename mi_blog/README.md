# Proyecto Django - Blog

## Instrucciones

1. Crear base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Crear superusuario:
```bash
python manage.py createsuperuser
```

3. Correr el servidor:
```bash
python manage.py runserver
```

## Funcionalidades

- `/crear_autor/`: formulario para crear autores
- `/crear_categoria/`: formulario para crear categorías
- `/crear_post/`: formulario para crear posts
- `/buscar_post/`: buscador de posts por título

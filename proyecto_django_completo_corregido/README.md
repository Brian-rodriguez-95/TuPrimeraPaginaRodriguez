
# Proyecto Django: Sistema de Pedidos Completo

Este proyecto está desarrollado con Django y cumple con los siguientes requisitos:

- Uso del patrón MVT (Model-View-Template).
- Definición de tres modelos: Cliente, Producto, Pedido.
- Formularios para insertar datos en cada modelo.
- Formulario para buscar clientes por nombre en la base de datos.
- Herencia de plantillas en HTML.
- Estructura lista para entrega y despliegue.

## Funcionalidades y cómo probar

1. Página de inicio: `/`  
2. Listar clientes: `/clientes/`  
3. Agregar nuevo cliente: `/clientes/nuevo/`  
4. Buscar clientes por nombre: `/clientes/buscar/`  
5. Listar productos: `/productos/`  
6. Agregar nuevo producto: `/productos/nuevo/`  
7. Listar pedidos: `/pedidos/`  
8. Agregar nuevo pedido: `/pedidos/nuevo/`  

## Instalación

```bash
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Autor

Proyecto académico para Coderhouse.

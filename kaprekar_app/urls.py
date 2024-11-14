from django.urls import path
from . import views  # Aquí sí importamos views de la aplicación

urlpatterns = [
    path('', views.kaprekar_view, name='kaprekar'),  # Define la vista en la URL raíz
]


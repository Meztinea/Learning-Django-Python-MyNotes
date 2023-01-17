from django.urls import path
from . import views

# url, nombre de la vista (función), nombre para identificarlo en el template
urlpatterns = [
    path('', views.index, name='index'),
    path('town/<int:id>', views.get_town, name='town')
]

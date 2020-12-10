from django.urls import path
from .views import (LibroListCreateView, LibroRetrieveUpdateDeleteView,
AutorListCreateView, AutorRetrieveUpdateDeleteView,
EditorialListCreateView, EditorialRetrieveUpdateDeleteView)

urlpatterns = [
    path('autores', AutorListCreateView.as_view(), name='autor-list-create'),
    path('autores/<int:pk>', AutorRetrieveUpdateDeleteView.as_view(), name='autor-details'),
    path('libros/', LibroListCreateView.as_view(), name='libro-list-create'),
    path('libros/<int:pk>', LibroRetrieveUpdateDeleteView.as_view(), name='libro-details'),
    path('editoriales', EditorialListCreateView.as_view(), name='editorial-list-create'),
    path('editoriales/<int:pk>', EditorialRetrieveUpdateDeleteView, name='editorial-details'),
]
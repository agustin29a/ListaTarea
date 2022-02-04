from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import ItemListView, ItemCreateView, ItemDetailView, Eliminar

urlpatterns = [
    path('', login_required(ItemListView.as_view()), name='list'),
    path('nuevo/', login_required(ItemCreateView.as_view()), name='create'),
    path('<int:pk>/', login_required(ItemDetailView.as_view()), name='detail'),
    path('delete/<id>/', Eliminar),
    
]

from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


from .models import Lista
from .forms import ListaForm

class ItemListView(ListView):
    model = Lista

    def get_queryset(self):
        queryset = Lista.objects.filter(user=self.request.user)
        name = self.request.GET.get('name', '-')
        state = self.request.GET.get('state', '-')
        description = self.request.GET.get('description', '-')
        if name != '-':
            queryset = queryset.filter(
                name__icontains=name
            )
        if state != '-':
            queryset = queryset.filter(
                state__icontains=state
            )    
        if description != '-':
            queryset = queryset.filter(
                description__icontains=description
            )       
        return queryset

    def now(self):
        return datetime.now().strftime('%Y-%m-%d')    


class ItemCreateView(CreateView):
    model = Lista
    form_class = ListaForm

    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)    

class ItemDetailView(UpdateView):
    model = Lista
    form_class = ListaForm
    template_name = 'lista_update.html'
    
    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)    

@login_required
def Eliminar(request, id):    
    item = Lista.objects.filter(user=request.user)
    item = item.get(pk=id)
    item.delete()
    return redirect('list')


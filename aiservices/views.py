from django.shortcuts import render
from django.views.generic.list import ListView
from .models import IAService

class IAServiceListView(ListView):
    template_name = 'registration/dashboard.html'
    queryset = IAService.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'Servicios contratados'
        context["IAServices"] = context['object_list']
        return context
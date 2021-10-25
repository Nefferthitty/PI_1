from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponse

from Controle.models import Oficio

class ViewOficio(CreateView):
    template_name = 'Controle/emissao.html'
    model = Oficio


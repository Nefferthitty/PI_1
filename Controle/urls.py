from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    #path('', views.ViewOficio.as_view(), name='oficio'),
    path('', TemplateView.as_view(template_name='emissao.html'), name='oficio'),
]
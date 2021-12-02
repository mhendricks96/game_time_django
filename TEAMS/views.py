from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Team
# Create your views here.

class HomeView(TemplateView):
  template_name = 'home.html'
  model = Team

class TeamList(ListView):
  template_name = 'team_list.html'
  model = Team

class TeamDetail(DetailView):
  template_name = 'team_list.html'
  model = Team
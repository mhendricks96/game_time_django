from django.urls import path
from django.urls.resolvers import URLPattern
from .views import TeamList, TeamDetail, HomeView

urlpatterns = [
  #path('', HomeView.as_view(), name='home'),
  path('team_list', TeamList.as_view(), name='team_list'),
  path('<int:pk>/', TeamDetail.as_view(), name='team_detail')
]
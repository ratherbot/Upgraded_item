from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('jobs/', views.collect_jobs, name='jobs'),
    path('vacancies/', views.collect_jobs, name='vacancies'),
    path('project_data/', views.collect_jobs, name='project_data'),
    path('statistics/', views.collect_jobs, name='statistics'),
]
from django.urls import path
from.views import  home,  projects, skills

urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects, name='projects'),
    path ('skills/', skills, name='skills'),

]
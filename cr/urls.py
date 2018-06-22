from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/info', views.registed, name='registed'),
    path('<int:student_id>/', views.register, name='register'),
]
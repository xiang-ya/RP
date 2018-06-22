from django.urls import path

from . import views

app_name = 'ratings'
urlpatterns = [
    path('rating/<int:professor_id>/<str:professor_name>/', views.professor_rating,
         name='professor_rating'),
]
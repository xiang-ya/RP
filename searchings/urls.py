from django.urls import path

from . import views

app_name = 'searchings'
urlpatterns = [
    path('<int:professor_id>/<str:professor_name>/', views.professor, name='professor'),
    path('school/<str:professor_school>/', views.school_filter, name='school_filter'),
    path('prof/<str:professor_name>/', views.professor_filter, name='professor_filter'),
    path('school_prof/<str:professor_school>/', views.school_professor_filter,
         name='school_professor_filter'),
    path('college_prof/<str:professor_college>/', views.college_professor_filter,
         name='college_professor_filter'),
]

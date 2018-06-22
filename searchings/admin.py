from django.contrib import admin
from .models import Professor, Rating, GeneralClass, College, Major, School

admin.site.register(Professor)
admin.site.register(GeneralClass)
admin.site.register(Rating)
admin.site.register(College)
admin.site.register(Major)
admin.site.register(School)

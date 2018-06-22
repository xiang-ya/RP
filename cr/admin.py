from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'student_info', 'school_name')

    def student_info(self, obj):
        return obj.school_id

    def get_queryset(self, request):
        queryset = super(StudentAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-school_name')
        return queryset

    student_info.short_description = 'INFO'


admin.site.register(Student, StudentAdmin)
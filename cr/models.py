from django.db import models
from django.contrib.auth.models import User


class Registration(models.Model):
    registration_state_choices = (
        ('rs', 'registration successful'),
        ('ru', 'registration unsuccessful'),
    )
    registration_state = models.CharField(max_length=3, choices=registration_state_choices, default='ru')
    class_registration = models.OneToOneField('searchings.SpecificClass', on_delete=models.CASCADE)
    registration_student = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.registration_student) + "\n" + \
               "registration state" + str(self.registration_state) + "\n" + \
               self.class_registration.class_introduction.class_name + \
               "\n" + str(self.class_registration.class_introduction.class_prof) + "\n" + \
               str(self.class_registration.class_introduction.class_college) \
               + self.class_registration.class_introduction.class_introduction + "\n" + \
               self.class_registration.class_introduction.class_type + "\n" + \
               str(self.class_registration.class_introduction.class_credit) + "\n" + \
               self.class_registration.class_introduction.class_prerequisite


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    major_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_image = models.ImageField(upload_to='profile_image', blank=True, default="profile_image/default.PNG")

    def __str__(self):
        return 'Student name: ' + self.last_name + ' ' + self.first_name


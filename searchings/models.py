from django.db import models
from django.contrib.auth.models import User


class Professor(models.Model):
    prof_name = models.CharField(max_length=30)
    prof_introduction = models.TextField()
    prof_school = models.ManyToManyField('School')
    prof_college = models.ManyToManyField('College')

    def __str__(self):
        return str(self.prof_name)


class School(models.Model):
    school_name = models.CharField(max_length=20)
    school_location = models.CharField(max_length=20, default='')
    school_introduction = models.TextField()

    def __str__(self):
        return self.school_name

    def __unicode__(self):
        return self.school_name


class College(models.Model):
    college_name = models.CharField(max_length=20)
    college_introduction = models.TextField()

    def __str__(self):
        return str(self.college_name)


class Major(models.Model):
    major_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.major_name)


class GeneralClass(models.Model):
    class_name = models.CharField(max_length=20)
    class_prof = models.ManyToManyField(Professor)
    class_college = models.ForeignKey(College, on_delete=models.CASCADE)
    class_major = models.ForeignKey("Major", on_delete=models.CASCADE)
    class_introduction = models.TextField()
    class_prerequisite = models.CharField(max_length=20)
    class_type = models.CharField(max_length=20)
    class_credit = models.FloatField()

    def __str__(self):
        return str(self.class_name)


class SpecificClass(models.Model):
    class_introduction = models.ForeignKey(GeneralClass, on_delete=models.CASCADE)
    class_section = models.IntegerField()
    class_code = models.IntegerField()
    class_period = models.CharField(max_length=20)
    class_remain_seat = models.IntegerField()

    def __str__(self):
        return self.class_introduction.class_name + '\n' + \
               str(self.class_introduction.class_prof) + '\n' + \
               str(self.class_introduction.class_college) + '\n' + \
               str(self.class_introduction.class_introduction) + '\n' + \
               str(self.class_section) + str(self.class_code) + '\n' + \
               str(self.class_remain_seat)


class Rating(models.Model):
    attendance_choices = (
        ('未知', "it's still a secret"),
        ('每周必点', "100% take attendance"),
        ('人少就点', "if there seems like not enough people"),
        ('基本不管', "doesn't really care the attendance"),
        ('纯看心情', "depends on the days or professor's mood"),
    )
    overall_rating = models.FloatField()
    overall_difficulty_number = models.FloatField()
    class_graded = models.CharField(max_length=5)
    overall_difficulty = models.CharField(max_length=100)
    overall_looking = models.CharField(max_length=20)
    attendance_requirement = models.CharField(max_length=30, choices=attendance_choices, default="未知")
    prof_personality_tag = models.CharField(max_length=50, null=True)
    student_learning_tag = models.CharField(max_length=50, null=True)
    class_atmosphere_tag = models.CharField(max_length=30, null=True)
    homework_requirement_tag = models.CharField(max_length=30, null=True)
    teaching_style_tag = models.CharField(max_length=30, null=True)
    prof_rating = models.ForeignKey('Professor', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.overall_rating) + '\n' + \
               str(self.overall_difficulty) + '\n' + \
               str(self.overall_looking) + '\n' + \
               str(self.class_graded) + '\n' + \
               str(self.attendance_requirement) + '\n' + \
               str(self.prof_personality_tag) + '\n' + \
               str(self.student_learning_tag) + '\n' + \
               str(self.class_atmosphere_tag) + '\n' + \
               str(self.homework_requirement_tag) + '\n' + \
               str(self.teaching_style_tag)


class Post(models.Model):
    post = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    rating_post = models.ForeignKey('Rating', on_delete=models.CASCADE)

    def __str__(self):
        return self.post

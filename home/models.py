from django.db import models


class Search(models.Model):
    school = models.CharField(max_length=200, default='')
    prof = models.CharField(max_length=200, default='')
    college = models.CharField(max_length=100, default='')




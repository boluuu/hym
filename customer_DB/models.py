from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length= 50)
    date = models.DateTimeField(auto_now_add=False)
    phone = models.CharField(max_length=11, default="")
    birthday = models.DateField(auto_now_add=False)
    email = models.EmailField()
    length = models.CharField(max_length=10, default="")
    shoulder_back = models.CharField(max_length=10, default="")
    chest = models.CharField(max_length=10, default="")
    stomach_fit = models.CharField(max_length=10, default="")
    sleeve = models.CharField(max_length=10, default="")
    bicep_arm = models.CharField(max_length=10, default="")
    cuff = models.CharField(max_length=10, default="")
    neck = models.CharField(max_length=10, default="")
    head = models.CharField(max_length=10, default="")
    length_trouser = models.CharField(max_length=10, default="")
    thigh = models.CharField(max_length=10, default="")
    waist = models.CharField(max_length=10, default="")
    ankle = models.CharField(max_length=10, default="")
    knee = models.CharField(max_length=10, default="")
    calf = models.CharField(max_length=10, default="")


    def __str__(self):
        return self.name


class Measurements(models.Model):
    length = models.FloatField()


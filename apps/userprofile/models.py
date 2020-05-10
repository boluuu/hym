from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, blank=True)
    birth_date = models.DateField(auto_now_add=False, blank=True, null=True, default=None)  #change to datepicker(auto_add_now)
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
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
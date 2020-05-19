from django.db import models

class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.firstname

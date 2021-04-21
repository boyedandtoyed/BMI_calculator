from django.db import models
<<<<<<< HEAD
# from django.core.validators import RegexValidator

# Create your models here.
=======
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.core.validators import RegexValidator

>>>>>>> e3fe231 (height bug correction)

# alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetical characters are allowed.')
# name = models.CharField(max_length=150, required=True, validators=[alpha])


class UserModel(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
	
    def __str__(self):
        return self.name + " " + f"{self.age}"
    
=======
    name = models.CharField(max_length=100) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    bmi = models.FloatField(null=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True)
    
	
    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def createUserModel(sender, instance, created, **kwargs):
    if created:
        UserModel.objects.create(user=instance)



>>>>>>> e3fe231 (height bug correction)

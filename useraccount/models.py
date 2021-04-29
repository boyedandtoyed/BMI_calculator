from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from BMIcalcapp.models import State
# from django.core.validators import RegexValidator

# alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetical characters are allowed.')
# name = models.CharField(max_length=150, required=True, validators=[alpha])


class UserModel(models.Model):

    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(default=5,null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    bmi = models.FloatField(null=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True)
    # email_confirmed = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def createUserModel(sender, instance, created, **kwargs):
    if created:
        # print(dir(instance),"/n/n/n/n/n/n--------------/n/n/n------", dir(sender))
        user = UserModel.objects.create(user=instance)
        user.email = instance.email
        user.name = instance.username
        user.save()
        




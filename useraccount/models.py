from django.db import models
# from django.core.validators import RegexValidator

# Create your models here.

# alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetical characters are allowed.')


    # name = models.CharField(max_length=150, required=True, validators=[alpha])

class UserModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
	
    def __str__(self):
        return self.name + " " + f"{self.age}"
    
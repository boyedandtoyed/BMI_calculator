from django.db import models


# class BMI(models.Model):
#     weight = models.IntegerField(null=True, blank=True)
#     height = models.IntegerField(null=True, blank=True)
#     currentBMI = models.IntegerField(null=True, blank=True)

#     def __str__(self):
#         return self.weight
# from django.db import models
# from useraccount.models import UserModel
# from django.dispatch import receiver
# from django.db.models.signals import post_save

# class BMI(models.Model):
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE, null=True)
#     weight = models.IntegerField(null=True, blank=True)
#     height = models.IntegerField(null=True, blank=True)
#     date = models.DateTimeField(auto_now_add=False)
#     updated_time = models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return self.weight


# @receiver(post_save, sender=UserModel)
# def bmiSave(sender, instance, created, **kwargs):
#     if created:
#         BMI.objects.create(user=instance)


# # class Suggestion(models.Model):
# #     underweight_condition = models.TextField(null=True, blank=True)
# #     normal_condition = models.TextField(null=True, blank=True)
# #     overweight_condition = models.TextField(null=True, blank=True)
# #     obese_condition = models.TextField(null=True, blank=True)

    
    

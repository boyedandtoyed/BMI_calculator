from django.db import models


class BMI(models.Model):
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    currentBMI = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.weight
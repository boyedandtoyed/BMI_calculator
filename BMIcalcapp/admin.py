from django.contrib import admin
from BMIcalcapp.models import State

# Register your models here.
# from BMIcalcapp.models import BMI # Suggestion


# admin.site.register(BMI)
# admin.site.register(Suggestion)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('state','lower_value','higher_value')



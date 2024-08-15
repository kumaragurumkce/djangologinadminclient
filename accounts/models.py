from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
class Profile(models.Model):
    ADMIN = 1
    CUSTOMER = 0

    USER_TYPE_CHOICES = [
        (ADMIN, 'Admin'),
        (CUSTOMER, 'Customer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=CUSTOMER)

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"

@admin.register(Profile)
class Admin(admin.ModelAdmin):
    list_display = ('user','user_type')
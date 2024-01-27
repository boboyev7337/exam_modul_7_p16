from django.contrib import admin

from app.models import UserPasswordManager


# admin.register(UserPasswordManager)
@admin.register(UserPasswordManager)
class UserPasswordManagerAdmin(admin.ModelAdmin):
    fields = ['__all__']
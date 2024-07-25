from django.contrib import admin

# Register your models here.
from recepe.models import*

admin.site.register(Recepies)
admin.site.register(UserRecord)
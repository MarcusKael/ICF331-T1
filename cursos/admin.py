from django.contrib import admin
from django.contrib.auth.models import user
from django.contrib.auth.models import Permission

# Register your models here.

admin.site.register(Permission)
u = User.objects.get(username__exact="Franco")
u.set_password("exrezeo6g7")
u.save()
u = User.objects.get(username__exact="FrancoBaez")
u.set_password("exrezeo6g7")
u.save()

from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Label)
admin.site.register(models.Entity)
admin.site.register(models.RelationShip)
admin.site.register(models.Label_RelationShip)


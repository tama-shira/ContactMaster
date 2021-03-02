from django.contrib import admin

# Register your models here.
from .models import System, NormalContact, FaultContact, LargeFaultContact

admin.site.register(System)
admin.site.register(NormalContact)
admin.site.register(FaultContact)
admin.site.register(LargeFaultContact)
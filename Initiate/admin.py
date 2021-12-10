from django.contrib import admin
from .models import Initiate
# Register your models here.

class InitiateAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Initiate, InitiateAdmin)

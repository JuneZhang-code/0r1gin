from django.contrib import admin
from .models import Designeraccount
# Register your models here.
from .models import Designerimage


class DesigneraccountAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Designeraccount, DesigneraccountAdmin)
admin.site.register(Designerimage)

from django.contrib import admin
from .models import IAService

class IAServiceAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    list_display = ('__str__', 'slug', 'created_at')


admin.site.register(IAService, IAServiceAdmin)

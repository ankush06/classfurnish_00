from django.contrib import admin

# Register your models here.

from .models import merchantProfile

class merchantProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name'],
        }),
    ]
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(merchantProfile, merchantProfileAdmin)



from django.contrib import admin
from models import developer, attendLog

class developerAdmin(admin.ModelAdmin):
    list_display = ('name', 'password')

admin.site.register(developer, developerAdmin)
admin.site.register(attendLog)
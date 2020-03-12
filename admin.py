from django.contrib import admin
from .models import EduabiertaInfo

class EduabiertaInfoAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    show_full_result_count = False
    search_fields = ('user__username', 'phone')
    list_display = ('id', 'user', 'phone')

admin.site.register(EduabiertaInfo, EduabiertaInfoAdmin)

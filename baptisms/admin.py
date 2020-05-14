from django.contrib import admin

from .models import Baptism

class BaptismAdmin(admin.ModelAdmin):
    list_display = ('id', 'bap_first_name','bap_middle_name','bap_last_name', 'date_of_birth', 'place_of_birth', 'fathers_name', 'mothers_name')
    list_display_links = ('id', 'bap_first_name', 'bap_middle_name', 'bap_last_name')
    search_fields = ('bap_last_name', 'fathers_name', 'mothers_name')
    list_per_page = 25

admin.site.register(Baptism, BaptismAdmin)

 
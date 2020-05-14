from django.contrib import admin

from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name','email', 'mobile_no')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'mobile_no')
    list_per_page = 25

admin.site.register(Member, MemberAdmin)

from django.contrib import admin

from .models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','phone','email','message','enquiry_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 25

admin.site.register(Enquiry, EnquiryAdmin)
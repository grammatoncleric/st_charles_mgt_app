from django.contrib import admin

from .models import Bookmass

class BookmassAdmin(admin.ModelAdmin):
    list_display = ('id', 'bookmass_time','fullname', 'mobile_no', 'names_to_pray_for', 'intention', 'intention_category', 'photo_pay_evidence')
    list_display_links = ('id', 'bookmass_time', 'fullname')
    search_fields = ('fullname', 'mobile_no', 'intention_category')
    list_per_page = 25

admin.site.register(Bookmass, BookmassAdmin)

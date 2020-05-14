
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('enquiries/', include('enquiries.urls')),
    path('baptisms/', include('baptisms.urls')),
    path('bookmasses/', include('bookmasses.urls')),
    path('members/', include('members.urls')),

]

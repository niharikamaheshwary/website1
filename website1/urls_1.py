
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from ITSP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ITSP/',include('ITSP.urls')),
    path('Team/', views.Teamlist.as_view()),
    path('Members/',views.Memberslist.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

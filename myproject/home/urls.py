from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('knowus',views.knowus,name="knowus"),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services')
]

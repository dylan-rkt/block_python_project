from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/",views.hello),
    path("about-us/",views.about),
    path('contact-us/', views.contact, name='contact'),
]

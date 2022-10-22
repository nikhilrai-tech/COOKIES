from django.contrib import admin
from django.urls import path
from mainapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('set/',views.set),
    path('get/',views.get),
    path('update/',views.update),
    path('delete/',views.delete),


]

from django.conf.urls import url
from django.urls import path
from.import views

urlpatterns = [
    path(r'',views.index),
    path('directory/',views.directory,name="directory"),
	path('directoryinfo/<int:pk>',views.directoryinfo,name="directoryinfo"),

]
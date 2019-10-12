from django.conf.urls import url
from django.urls import path
from.import views

urlpatterns = [
	#path(r'',views.index),
	path('vecancy/',views.vacancy, name="job"),
	path('vecancyinfo/<int:pk>', views.vacancyinfo, name="vecancyinfo"),
	path('About/',views.About,name="About"),
	path('help/',views.help1,name="help"),
	path('feedback/',views.feedback1,name="feedback"),

]
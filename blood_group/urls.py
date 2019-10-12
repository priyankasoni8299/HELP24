from django.conf.urls import url
from django.urls import path
from.import views

urlpatterns = [
	path(r'',views.index),
	path('bloodbank/',views.bloodbank,name="bloodbank"),
	path('donarinfo/',views.donarinfo,name="donarinfo"),
	path('donar/',views.donarregistration,name="donarregistration"),
	path('donorsearch/',views.donorsearch,name="donorsearch"),
]
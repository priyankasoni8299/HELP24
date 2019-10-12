from django.conf.urls import url
from django.urls import path
from.import views

urlpatterns = [
    path(r'',views.index),
    path('bnews/<int:pk>',views.breakingnewsdata,name="breakingnewsdata"),
	path('nuser/',views.newsuser,name="newsuser"),
	#path('table/',views.table,name="table"),	
]
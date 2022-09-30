from django.urls import path
from . import views 

urlpatterns = [
	path('',views.home,name = 'home'),
	path('about/',views.about,name = 'about'),
	path('modi/',views.modi,name='modi'),
	path('counter/',views.counter,name='counter'),
	path('mail1/',views.mail1,name='mail1'),
	path('mail2/',views.mail2,name='mail2')
]

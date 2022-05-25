from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="index"),
	path('elements/', views.elements, name="elements"),
	path('blog/', views.blog, name="blog"),
	path('events/', views.events, name="events"),
	path('contact/', views.contact, name="contact"),
	path('submitted_contact/', views.submitted_contact, name="submitted_contact"),
	path('album_store/', views.album_store, name="album_store"),
]
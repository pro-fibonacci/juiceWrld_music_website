from django.urls import path
from users import views

urlpatterns = [
        #Leave as empty string for base url

	path('login/', views.login, name="login"),
	path('register/', views.register, name="register"),
	path('logout/', views.logout, name="logout"),
]
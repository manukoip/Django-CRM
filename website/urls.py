
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    # We are not using tis as Login is implemented on the Home page
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]

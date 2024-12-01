from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('my_data/', views.my_data, name='my_data'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]

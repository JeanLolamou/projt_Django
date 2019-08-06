from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/signin.html' ,extra_context={'logoutMess':"You're now logged out"}), name='logout'),
    path('delete/<int:p_id>', views.delete, name='delete_product'),

]

from django.urls import path
from . import views
urlpatterns = [
    path('sign_up', views.UserRegistrationView.as_view(), name='sign_up'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path('deposit', views.DepositMoneyView.as_view(), name='deposit'),
]

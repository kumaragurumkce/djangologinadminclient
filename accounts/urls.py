from django.urls import path
from .views import register, user_login, user_logout,company_page,product_page,home

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('company_page/', company_page, name='company_page'),  
    path('product_page/', product_page, name='product_page'),
    path('', home, name='home'),  # Home page
  
]

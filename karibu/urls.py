from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

urlpatterns = [

    # ... your existing paths ...
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.log_out, name = 'logout'),
    path('home/<int:product_id>/',views.product_detail, name = 'product_detail'),
    path('product/<int:product_id>/edit/', views.edit_detail, name='edit_detail'),
    path('delete/<int:product_id>/',views.delete_detail, name = 'delete_detail'),
    path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),
    path('receipt/', views.receipt, name='receipt'),
    path('receipt/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('all_sales/', views.all_sales, name='all_sales'),
    path('deffered_payments/', views.deffered_payments, name='deffered_payments'),
    path('deffered_payments_list/', views.deffered_payments_list, name='deffered_payments_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('receipt_detail/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('record_sales/', views.record_sales, name='record_sales'),
    path('add_to_stock/<str:pk>/', views.add_to_stock, name='add_to_stock'),
    path('signup/', views.signup, name='signup'),

    # Admin dashboard (superuser/staff)
    path('owner_dashboard/', views.owner_dashboard, name='owner_dashboard'),

    # Manager dashboard (users in "Manager" group)
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),

    # Sales Agent dashboard (users in "SalesAgent" group)
    path('salesagent_dashboard/', views.salesagent_dashboard, name='salesagent_dashboard'),

    # Profile redirect
    path('accounts/profile/', views.profile_redirect, name='profile_redirect'),

]

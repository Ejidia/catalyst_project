"""
URL configuration for kgl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# kgl/urls.py  (project-level)
from django.contrib import admin
from django.urls import path
from karibu import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('home/', views.home, name='home'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='ebook/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('Login/', views.Login, name='Login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
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
    # remove duplicate receipt_detail route
    path('record_sales/', views.record_sales, name='record_sales'),
    path('add_to_stock/<str:pk>/', views.add_to_stock, name='add_to_stock'),
    path('signup/', views.signup, name='signup'),

    # Admin dashboard (superuser/staff)
    path('owner_dashboard/', views.owner_dashboard, name='owner_dashboard'),

    # Manager dashboard (users in "Manager" group)
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),

    # Sales Agent dashboard (users in "SalesAgent" group)
    path('salesagent_dashboard/', views.salesagent_dashboard, name='salesagent_dashboard'),

    path('receipt/final/<int:receipt_id>/', views.final_receipt, name='final_receipt'),

]

      




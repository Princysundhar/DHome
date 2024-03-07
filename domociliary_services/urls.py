"""my_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

from domociliary_services import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add_area',views.add_area),
    path('add_area_post',views.add_area_post),
    path('add_staff',views.add_staff),
    path('add_staff_post',views.add_staff_post),
    path('add_catogory',views.add_category),
    path('add_category_post',views.add_category_post),
    path('allocate_service',views.allocate_service),
    path('area_allocation',views.area_allocation),
    path('view_payment/<id>',views.view_payment),
    # path('view_allocatedservice',views.view_allocatedservice),
    path('view_allocation',views.view_allocation),
    path('view_area',views.view_area),
    path('view_category',views.view_category),
    path('view_staff',views.view_staff),
    path('',views.login_table),
    path('login_post',views.login_post),
    path('admin_home',views.admin_home),
    path('admin_edit_category/<id>',views.admin_edit_category),
    path('admin_edit_category_post/<id>',views.admin_edit_category_post),
    path('admin_edit_city/<id>',views.admin_edit_city),
    path('admin_edit_city_post/<id>',views.admin_edit_city_post),
    path('admin_edit_staff/<id>',views.admin_edit_staff),
    path('admin_edit_staff_post/<id>',views.admin_edit_staff_post),
    path('delete_category/<id>',views.delete_category),
    path('delete_city/<id>',views.delete_city),
    path('delete_staff/<id>', views.delete_staff),
    path('area_allocation_post',views.area_allocation_post),
    path('area_allocated',views.area_allocated),
    path('view_request',views.view_request),
    path('alct_staff/<id>',views.alct_staff),
    path('alct_staff_post/<id>',views.alct_staff_post),
    path('add_service',views.add_service),
    path('add_service_post',views.add_service_post),
    path('view_service',views.view_service),
    path('delete_service/<id>',views.delete_service),
    path('edit_service/<id>',views.edit_service),
    path('edit_service_post/<id>',views.edit_service_post),
    path('cancel_allocation_status/<id>',views.cancel_allocation_status),
    path('Staff_home',views.Staff_home),
    path('view_profile',views.view_profile),
    path('view_allocated_area',views.view_allocated_area),
    path('view_allocated_work_verified',views.view_allocated_work_verified),
    path('view_allocated_work_verify', views.view_allocated_work_verify),
    path('approve/<id>',views.approve),
    path('reject/<id>',views.reject),
    path('update_status/<id>',views.update_status),
    path('logout',views.logout),
    path('delete_allocation/<id>',views.delete_allocation),


    #................................................................................
    path('and_login',views.and_login),
    path('android_user_registration',views.android_user_registration),
    path('android_change_password',views.android_change_password),
    path('customer_view_category',views.customer_view_category),
    path('and_view_service',views.and_view_service),
    path('and_send_request',views.and_send_request),
    path('and_view_request',views.and_view_request),
    path('and_offline_payment',views.and_offline_payment),
    path('android_online_payment',views.android_online_payment),
    path('and_view_allocated_staff',views.and_view_allocated_staff),
    path('and_send_Feedback',views.and_send_Feedback),
    path('and_view_feedback',views.and_view_feedback),
    path('and_delete_feedback',views.and_delete_feedback),


]


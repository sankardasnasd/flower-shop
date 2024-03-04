
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.public_home), 
    path('public_login',views.public_login),
    path('admin_home',views.admin_home), 
    path('staff_home',views.staff_home), 
    path('staff_home',views.staff_home),
    path('customer_home',views.customer_home),
    path('admin_manage_staff',views.admin_manage_staff),
    path('admin_update_staff/<id>',views.admin_update_staff),
    path('public_signup',views.public_signup),
    path('admin_manage_vendor',views.admin_manage_vendor),
    path('admin_update_vendor/<id>',views.admin_update_vendor),
    path('admin_manage_category',views.admin_manage_category),
    path('admin_update_category/<id>',views.admin_update_category),
    path('item_view_more/<id>',views.item_view_more),

    path('active_item/<id>',views.active_item),
    path('deactive_item/<id>',views.deactive_item),
    path('active_staff/<id>',views.active_staff),
    path('inactive_staff/<id>',views.inactive_staff),
    path('add_flower/<id>',views.add_flower),

    path('admin_view_order', views.admin_view_order),
    path('admin_view_order_more/<id>', views.admin_view_order_more),
    path('admin_view_purchase', views.admin_view_purchase),

    path('admin_manage_item',views.admin_manage_item),
    path('admin_update_item/<id>',views.admin_update_item),
    path('admin_manage_flower',views.admin_manage_flower),
    path('admin_update_flower/<id>',views.admin_update_flower),
    path('admin_view_customer',views.admin_view_customer),
    path('admin_view_review',views.admin_view_review),


    path('staff_view_review',views.staff_view_review),
    path('staff_view_purchase',views.staff_view_purchase),

    path('staff_view_order',views.staff_view_order),
    path('staff_update_order/<id>',views.staff_update_order),

    path('staff_manage_vendor',views.staff_manage_vendor),
    path('staff_update_vendor/<id>',views.staff_update_vendor),
    path('staff_view_customer',views.staff_view_customer),
    path('staff_manage_category',views.staff_manage_category),
    path('staff_update_category/<id>',views.staff_update_category),
    path('staff_manage_flower',views.staff_manage_flower),
    path('staff_update_flower/<id>',views.staff_update_flower),

    path('staff_manage_item',views.staff_manage_item),
    path('staff_active_item/<id>',views.staff_active_item),
    path('staff_deactive_item/<id>',views.staff_deactive_item),

    path('staff_update_item/<id>',views.staff_update_item),
    path('staff_item_view_more/<id>',views.staff_item_view_more),



    path('customer_manage_review/<id>',views.customer_manage_review),
    path('customer_view_orders',views.customer_view_orders),
    path('customer_view_profile',views.customer_view_profile),
    path('edit_profile',views.edit_profile),
    path('bill/<id>',views.bill),
    path('customer_cart_customization/<id>',views.customer_cart_customization),
    path('view_customization/<id>',views.view_customization,name="view_customization"),
    path('customer_view_products',views.customer_view_products),
    path('customer_cart',views.customer_cart),
    path('order_fill/<id>',views.order_fill),
    path('add_cart/<id>',views.add_cart),
    path('remove_cart/<id>',views.remove_cart),
    path('increase_qty/<id>',views.increase_qty),
    path('decrease/<id>',views.decrease),
    path('payment/<id>',views.payment),
    path('cust_view_bill/<id>',views.cust_view_bill),
    path('increase_quantity_cust/<id>',views.increase_quantity_cust),


    path('assign_dellivery/<id>',views.assign_dellivery),
    path('staff_assign_dellivery/<id>',views.staff_assign_dellivery),
    path('add_purchase/<id>',views.add_purchase),
    path('staff_add_purchase/<id>',views.staff_add_purchase),

    path('admin_view_customization/<id>', views.admin_view_customization),

]


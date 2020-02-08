from django.urls import path
from using_api_view import views

urlpatterns = [
    path('category_av', views.catgory_av_list),
    path('category_av/<int:pk>', views.catgory_av_detail),
    path('sub_category_av', views.sub_category_av_list),
    path('sub_category_av/<int:pk>', views.sub_category_av_detail),
    path('vendor_av', views.vendor_av_list),
    path('delivery_av', views.delivery_av_list),
]
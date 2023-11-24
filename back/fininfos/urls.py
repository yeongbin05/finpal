from django.urls import path
from . import views

urlpatterns = [
    path('deposit-products/<int:page_pk>', views.deposit_products),
    path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/detail/<int:product_pk>', views.deposit_products_detail),
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_products_options),
    path('deposit-products/top_rate/', views.top_rate),
    path('deposit-products/saving_products/<int:page_pk>', views.saving_products),
    path('deposit-products/saving_product/<int:saving_pk>', views.saving_products_detail),
    path('deposit-products-options/saving_products/<str:fin_prdt_cd>', views.saving_products_options),
    path('deposit-products/save_saving_products/', views.save_saving_products),
    path('recommend/', views.recommend),
    path('recommend2/', views.recommend2),
    path('deposit-products/save_saving_products/', views.save_saving_products),
    path('deposit-products/<str:username>/<int:depositproducts_pk>/likes/', views.deposit_likes, name='deposit_likes'),
    path('deposit-products/<str:username>/<int:savingproducts_pk>/likes/', views.saving_likes, name='saving_likes'),
    # path('api_test/', views.api_test),
]

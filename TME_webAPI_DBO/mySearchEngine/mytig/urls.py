from django.urls import path
from mytig import views

urlpatterns = [
    path('products/', views.RedirectionListeDeProduits.as_view()),
    path('product/<int:pk>/', views.RedirectionDetailProduit.as_view()),
    path('onsaleproducts/', views.PromoList.as_view()),
    path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view()),
    path('shipPoints/', views.RedirectionListeDeShippoints.as_view()),
    path('shipPoint/<int:pk>/', views.RedirectionDetailShippoint.as_view()),
    path('availableproducts/', views.RedirectionListeDeIsAvailableProducts.as_view()),
    path('availableproduct/<int:pk>/', views.RedirectionListeDeIsAvailableProduct.as_view()),
]

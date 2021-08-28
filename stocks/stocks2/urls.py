from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('searchLiveRates', views.searchLiveRates, name="searchLiveRates"),
    path('buyStock', views.buyStock, name="buyStock"),
    path('sellStock/<stockId>', views.sellStock, name="sellStock"),
    path('login', views.login, name="login"),
    path('addToWallet', views.addToWallet, name="addToWallet")
]
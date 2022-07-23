from django.urls import path

from search_app.views import SearchResult
from . import views

app_name = 'shop'

urlpatterns = [
               path('', views.allProdCat, name='allProdCat'),
               path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
               path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]



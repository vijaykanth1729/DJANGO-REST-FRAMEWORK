from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import products_list
from .views import (product_detail,
                    AnimalApiView,
                    AnimalDetailApiView,
                    MovieListCreateView,
                    MovieRetrieveUpdateDestroyView,
                    MovieList,
                    MovieDetail,
                    )

app_name = 'products'

urlpatterns = [
    path('products/', products_list),
    path('products/<int:pk>/', product_detail),
    path('animals/', AnimalApiView.as_view()),
    path('animals/<int:id>/', AnimalDetailApiView.as_view()),
    path('movies/',MovieListCreateView.as_view()),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view())
    #path('moviesList/', MovieList.as_view()),
    #path('moviesDetail/<int:pk>/', MovieDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

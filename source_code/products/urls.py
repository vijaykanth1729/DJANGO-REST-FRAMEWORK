from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path,include
from .views import products_list, LoginView, LogoutView
from .views import (product_detail,
                    AnimalApiView,
                    AnimalDetailApiView,
                    MovieListView,
                    MovieDetailView,
                    MovieList,
                    MovieDetail,
                    )
app_name = 'products'

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    # path('products/', products_list),
    # path('products/<int:pk>/', product_detail),
    # path('animals/', AnimalApiView.as_view()),
    # path('animals/<int:id>/', AnimalDetailApiView.as_view()),
    # path('movies/',MovieListView.as_view()),
    # path('movies/<int:pk>/', MovieDetailView.as_view()),
    #
    # path('moviesList/', MovieList.as_view()),
    # path('moviesDetail/<int:pk>/', MovieDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

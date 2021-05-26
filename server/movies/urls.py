from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list_create),
    path('movie_list/', views.movie_list),
    path('<int:movie_id>/likes/', views.likes),
    path('<int:movie_id>/review_list/', views.review_list),
    path('<int:movie_id>/review_create/', views.review_create),
    path('<int:movie_id>/review/', views.review_update_delete),
    # path('<username>/rating/', views.movie_rate),
    # path('tmp/', views.tmp),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list_create),
    path('movie_list/', views.movie_list),
    path('<int:movie_id>/likes/', views.likes),
    path('<int:movie_id>/review_list/', views.review_list),
    path('<int:movie_id>/review_create/', views.review_create),
    path('reviews/<int:comment_pk>/', views.review_update_delete),
    path('reviews/<int:comment_pk>/reply_list/', views.reply_list),
    path('reviews/<int:comment_pk>/reply_create/', views.reply_create),
    path('replies/<int:reply_pk>/', views.reply_update_delete),
    path('<int:movie_id>/rating/', views.movie_rate),
    path('review_user/', views.review_user),
    path('reply_user/', views.reply_user),
    # path('tmp/', views.tmp),
]

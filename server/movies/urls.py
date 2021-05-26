from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list_create),
    path('movie_list/', views.movie_list),
    path('<int:movie_id>/likes/', views.likes),
    path('<int:movie_id>/review_list/', views.review_list),
    path('<int:movie_id>/review_create/', views.review_create),
    path('<int:movie_id>/review/<int:comment_pk>', views.review_update_delete),
    path('<int:movie_id>/review/<int:comment_pk>/list', views.reply_list),
    path('<int:movie_id>/review/<int:comment_pk>/reply/', views.reply_create),
    path('<int:movie_id>/review/<int:comment_pk>/reply/<int:reply_pk>/', views.reply_update_delete),
    # path('<int:movie_id>/rating/<username>/', views.movie_rate),
    # path('tmp/', views.tmp),
]

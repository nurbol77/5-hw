from django.urls import path

from movie_app import views

urlpatterns = [
    #path('director/', views.DirectorAPIView.as_view()),
    path('director/', views.DirectorAPIView.as_view()),
    path('director/<int:id>', views.DirectorDetailAPIViwe.as_view()),
    #path('movie/', views.movie_list),
    path('movie/', views.MovieAPIView.as_view()),
    path('movie/<int:id>', views.MovieDetelAPIView.as_view()),
    path('review/', views.ReviewAPIView.as_view()),
    path('review/<int:id>', views.ReviewDetailAPIView.as_view()),


]

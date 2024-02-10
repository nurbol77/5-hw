from django.urls import path

from . import views
from .views import *

# urlpatterns = [
#     path('register/', views.register),
#     path('confirm/', views.confirm),
#     path('Login/', views.Login_view),
#
# ]


urlpatterns = [
    path('register/', views.register),
    path('confirm/', views.confirm),
    path('login/', views.login_view),

]

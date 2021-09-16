from django.urls import path
from .views.world_views import Worlds, WorldDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('worlds/', Worlds.as_view(), name='worlds'),
    path('worlds/<int:pk>/', WorldDetail.as_view(), name='world_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]

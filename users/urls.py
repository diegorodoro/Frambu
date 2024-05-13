from django.urls import path
from .views import login_user,logout_user, SignUpView


urlpatterns = [
    path('', login_user, name='login'),
    path('logout_user', logout_user, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

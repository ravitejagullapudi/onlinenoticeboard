from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.login_view,name='login'),
    path('register/',views.register,name='register'),
    path('login_rej/',views.login_rejected,name='login_rej'),
    path('logout/',views.logout_view,name='logout'),
]
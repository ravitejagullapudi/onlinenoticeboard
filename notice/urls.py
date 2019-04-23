from django.contrib import admin
from django.urls import path
from notice import views

urlpatterns=[
    path('',views.index,name='index'),
    path('post_notice/',views.post_notice,name='post_notice'),
    path('post_notice1/',views.post_notice1,name='post_notice1'),
    path('post_sucess/',views.post_sucess,name='post_sucess'),
    path('view_notice/',views.view_notice,name='view_notice'),
    path('notice_info/<int:notice_id>',views.notice_info,name='notice_info'),

    path('st/',views.index1,name='index1'),
    path('view_notice1/',views.view_notice1,name='view_notice1'),
    path('notice_info1/<int:notice_id>',views.notice_info1,name='notice_info1'),
]
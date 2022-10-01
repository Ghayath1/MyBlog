from django.urls import path
from .views import post_detail,post_list,edit_post,delete_post,new_post

urlpatterns = [
   
    path('',post_list,name='all_posts'),
    path('new',new_post,name='new_post'),
    path('<int:id>',post_detail,name='post_detail'),
    path('<int:id>/edit',edit_post,name='edit_post'),
    path('<int:id>/delete',delete_post,name='delete_post'),
]

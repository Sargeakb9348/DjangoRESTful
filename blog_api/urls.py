from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [ #two API enpoints (PostList and PostDetail)
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), #takes in an integer primary key (a view that will show one record)
    path('', PostList.as_view(), name='listcreate'), #displays whole database (all posts)
]
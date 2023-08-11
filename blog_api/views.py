from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
# Create your views here.

class PostList(generics.ListCreateAPIView): #list or create items
    queryset = Post.postobjects.all()#return all posts that are flagged as published
    serializer_class = PostSerializer#serializers formats different types of data into an easier format to be converted to JSON
    pass

class PostDetail(generics.RetrieveDestroyAPIView): #retrieve or delete item
    pass

""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
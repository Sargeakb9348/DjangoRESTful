from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer): #extending from serializer, modelserializer
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status') #define what data in the model we want to work with
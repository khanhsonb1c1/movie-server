from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def index(request):

    return Response({"Success": "The setup was successfully"})


@api_view(['GET'])
def getAllPosts(request):
    getPosts = Post.objects.all()
    serializers = PostSerializer(getPosts, many=True)

    return Response(serializers.data)


@api_view(['POST'])
def createPost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The post was successfully created"}, status=201)

    else:
        return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def deletePost(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return Response({"Success": "Deleted"})

    except Post.DoesNotExit:
        return Response({"Error": "The post does not exit"})
    
    
@api_view(['GET'])
def getDetailPost(request, id):
    try:
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    except Post.DoesNotExit:
        return Response({"Error": "The post does not exit"})
    
@api_view(['PUT'])
def updatePost(request,id):
    
    new_title = request.data.get('title')
    new_content = request.data.get('content')

    try:
        post = Post.objects.get(id=id)
        
        if new_title:
            post.title = new_title
        if new_content:
            post.content = new_content
            
        post.save()
        
        return Response({"Success": "Updated"})
 

    except Post.DoesNotExit:
        return Response({"Error": "The post does not exit"})

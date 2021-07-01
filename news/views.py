from .models import Article
from .serializers import ArticleSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import Http404
"""
@api_view(["GET","POST"])
def article_list(request):
    if request.method=="GET":#wyswietlanie artykulow
        articles = Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    elif request.method=="POST":#tworzenie artykulu
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleList(generics.ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

"""
class ArticleList(APIView):
    def get(self,request):
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)#przypisuje uzytkownika do artykulu
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
"""
@api_view(["GET","PUT","DELETE"])
def article_detail(request,articleId):
    try:
        article= Article.objects.get(pk=articleId)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =="GET":
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method =="PUT":
        serializer=ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    elif request.method=="DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
class ArticleDetail(APIView):
    def  get_article(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404
    
    def is_owner(self,request,object):
        return object.owner==request.user

    def get(self,request,pk):
        serializer=ArticleSerializer(self.get_article(pk))
        return Response(serializer.data)
          
    def put(self,request,pk):
        article=self.get_article(pk)
        if self.is_owner(request,article): 
            serializer=ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"response":"You don't have permission to edit this object"})
    
    def delete(self,request,pk):
        article=self.get_article(pk)
        if self.is_owner(request,article):
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"response":"You don't have permission to delete this object"})
    

# Create your views here.
"""
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
 """

class ListUser(APIView):
    def get(self,request):
        if request.user.is_superuser:
            #if request.user.is_staff:
            users=User.objects.all()
            serializer=UserSerializer(users,many=True)
            return Response(serializer.data)
        else:
            return Response({"response":"You don't have permission to view this object"})
    

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

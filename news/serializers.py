from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article 
        fields=("id","title","email","date","owner")
        read_only_fields=("owner",)
class UserSerializer(serializers.ModelSerializer):
    articles=serializers.PrimaryKeyRelatedField(many=True,queryset=Article.objects.all())
    class Meta:
        model = User
        fields=("id","username","password","articles")
    
    def create(self,validated_data):
        user=User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
    
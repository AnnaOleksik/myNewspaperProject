from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
#title,email,owner(user kt utworzyl artykul)
class Article(models.Model):
    title=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="articles")

    def __str__(self):
        return self.title + " " + str(self.date)


#tworzenie tokena dla kazdego tworzonego uzytkownika
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)


# Create your models here.



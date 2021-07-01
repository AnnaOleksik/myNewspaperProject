from django.urls import path
from . import views
urlpatterns=[
    #path("articles/",views.article_list),
    path("articles/",views.ArticleList.as_view()),
    #path("articles/<int:articleId>",views.article_detail),
    path("articles/<int:pk>",views.ArticleDetail.as_view()),
    path("register/",views.ListUser.as_view()),
]
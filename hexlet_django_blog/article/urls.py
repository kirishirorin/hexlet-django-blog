from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('<str:tags>/<int:article_id>/', views.med_info_view, name='article')
]

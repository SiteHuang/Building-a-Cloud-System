# Team 20
# Team member: Site Huang, 908282
#              Chenyuan Zhang, 815901
#              Zixuan Zhang, 846305
#              Zhentao Zhang, 864735
#              Kangyun Dou, 740145

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('wrath', views.wrath, name='wrath'),
    path('pride', views.pride, name='pride'),
    path('hashtags', views.hashtags, name='hashtags'),
    path('api/v1/sentiment_by_suburbs', views.sentiment_by_suburbs, name='sentiment_by_suburbs'),
    path('api/v1/sentiment_by_weekdays', views.sentiment_by_weekdays, name='sentiment_by_weekdays'),
    path('api/v1/sentiment_by_hours', views.sentiment_by_hours, name='sentiment_by_hours'),
    path('api/v1/word_cloud', views.word_cloud, name='word_cloud'),
    path('aurin', views.aurin, name='aurin'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('report', views.report, name='report'),
]

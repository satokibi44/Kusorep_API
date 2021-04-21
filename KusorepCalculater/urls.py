from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.kusorep_score_viewset, name='kusorep_score_viewset'),
]

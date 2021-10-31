from django.urls import path
from .views import HomePageView,StudyGroup

urlpatterns = [
    path("", HomePageView, name="home"),
    path("study-group/", StudyGroup, name="study-group"),
]
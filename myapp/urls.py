from django.urls import path
from .views import Home , detail_blog

urlpatterns = [
      path("", Home.as_view(), name="home"),
       path("/blogdetail/<int:id>", detail_blog, name="detail"),

]

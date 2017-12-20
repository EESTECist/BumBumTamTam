from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.post, name="post"),
    path("<slug:category_slug>/", views.category, name="category")
]

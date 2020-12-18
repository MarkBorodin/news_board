from django.urls import path
from .views import CommentCreateView, Index, to_vote

app_name = "news_board"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("comment_create/<int:pk>", CommentCreateView.as_view(), name="comment_create"),
    path("to_vote/<int:pk>", to_vote, name="to_vote"),
]

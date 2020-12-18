from django.urls import path

from news_board.api.views import (
    NewsListCreateView,
    CommentListCreateView,
    CommentUpdateDeleteView,
    NewsUpdateDeleteView,
    VoteUpdateView,
)


app_name = "api_news_board"

urlpatterns = [
    # news:
    path("news/", NewsListCreateView.as_view(), name="news_list"),
    path("news/<int:pk>/", NewsUpdateDeleteView.as_view(), name="news_update"),
    path("news/<int:pk>/upvotes/", VoteUpdateView.as_view(), name="news_vote"),
    # comments:
    path(
        "news/<int:pk>/comments/", CommentListCreateView.as_view(), name="comments_list"
    ),
    path(
        "news/<int:pk>/comments/<int:comment_pk>/",
        CommentUpdateDeleteView.as_view(),
        name="comment_update_delete",
    ),
]

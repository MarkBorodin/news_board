from rest_framework import generics

from rest_framework.generics import get_object_or_404

from news_board.api.serializers import NewsVoutesSerializer


from news_board.api.serializers import NewsSerializer, CommentSerializer
from news_board.models import News, Comment


class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class VoteUpdateView(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsVoutesSerializer

    def put(self, request, *args, **kwargs):
        news = News.objects.get(id=self.kwargs["pk"])
        news.amount_of_upvotes += 1
        news.save()
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)


class NewsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(news=self.kwargs["pk"])
        return queryset


class CommentUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_object(self):
        queryset = self.get_queryset()
        news_id = self.kwargs.get("pk")
        comment_id = self.kwargs.get("comment_pk")
        return get_object_or_404(queryset, news__id=news_id, id=comment_id)

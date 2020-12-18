from django.shortcuts import redirect

from .models import News, Comment
from .forms import CommentForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy


class Index(ListView):
    model = News
    context_object_name = "news_list"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = News.objects.all()
        context["comments"] = Comment.objects.all()
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy("news_board:index")
    template_name = "create_comment.html"
    context_object_name = "comment"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = News.objects.get(id=self.kwargs["pk"])
        return context

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST["news"] = self.kwargs["pk"]
        request.POST._mutable = False
        return super().post(request, *args, **kwargs)


def to_vote(request, pk):
    result = News.objects.get(id=pk)
    result.amount_of_upvotes += 1
    result.save()
    return redirect("news_board:index")

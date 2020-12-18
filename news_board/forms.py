from .models import News, Comment
from django import forms
from django.forms import ModelForm


class CommentForm(ModelForm):
    news = forms.ModelChoiceField(queryset=News.objects.all())

    class Meta:
        model = Comment
        fields = ["text", "comment_author_name", "news"]

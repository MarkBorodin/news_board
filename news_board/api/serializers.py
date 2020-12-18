from rest_framework import serializers

from news_board.models import News, Comment


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "link",
            "amount_of_upvotes",
            "author_name",
            "create_date",
        )


class NewsVoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("amount_of_upvotes",)

        read_only_fields = ("amount_of_upvotes",)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "news", "comment_author_name", "text", "create_date")

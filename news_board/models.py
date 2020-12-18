from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField(null=True, auto_now_add=True)


class News(BaseModel):
    title = models.CharField(max_length=256, null=False, blank=False)
    link = models.URLField(
        max_length=256,
        null=False,
        blank=False,
    )
    amount_of_upvotes = models.SmallIntegerField(default=0)
    author_name = models.CharField(
        max_length=128, null=False, blank=False, default="unknown author"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
        ordering = ["-amount_of_upvotes", "create_date"]


class Comment(BaseModel):
    news = models.ForeignKey(to=News, on_delete=models.CASCADE, related_name="comments")
    comment_author_name = models.CharField(
        max_length=128, null=False, blank=False, default="unknown user"
    )
    text = models.TextField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.text

from celery import shared_task

from news_board.models import News


@shared_task
def del_votes():  # noqa
    news = News.objects.all()
    for some_news in news:
        some_news.amount_of_upvotes = 0
        some_news.save()

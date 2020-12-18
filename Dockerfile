FROM python:3.8

RUN apt-get update
RUN apt-get install git

RUN mkdir -p /srv/commands
WORKDIR /srv

COPY ./app ./
COPY ./news_board ./
COPY ./manage.py ./
COPY ./commands/ ./commands
COPY ./requirements.txt ./
COPY ./manage.py ./

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]

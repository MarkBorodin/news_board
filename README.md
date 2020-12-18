# News board


### With this web application, you can view the list of news with the ability to vote for them and comment on them.
### Application provides СRUD API to manage news posts and comments to them. 
### It is possible to vote for news. Once a day, all news votes are reset.


## INSTALL_NEWS_BOARD

### Setup

### set up environment

Clone the repository to the remote machine and install Docker. 
Then, create a file ".env" 
```
touch .env
```
and fill in the file as in the example ".env.example", but with your own settings. Where "xxxx" you need to change to your settings (use "nano .env" to edit this file)


### run app

run:

```
docker-compose up
```

you need to create database:
```
docker-compose exec postgresql bash
```
next step:
```
su - postgres
```
next step:
```
psql
```
next step (you can create your own user, change password and other data):
```
CREATE DATABASE news_board; 
CREATE USER news_board_admin WITH PASSWORD 'xxxx';
ALTER ROLE news_board_admin SET client_encoding TO 'utf8';
ALTER ROLE news_board_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE news_board_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE news_board TO news_board_admin;
ALTER USER news_board_admin CREATEDB;

```
return in to folder "news_board" (use combination of keys "ctrl + d" 3 times)

you need to add your changed data in ".env" file (use nano .env) 

you shout make migration:
```
docker-compose exec backend python manage.py migrate
```

### Finish


## API Documentation:

News_board API Documentation https://documenter.getpostman.com/view/12740553/TVsoJWiD


## Postman collection:

https://www.getpostman.com/collections/60fa0d240bcfcdfdee6f

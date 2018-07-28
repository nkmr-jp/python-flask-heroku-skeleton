# Python Flask Heroku Skeleton

## Install to Mac

1. install python.
[anaconda](https://www.anaconda.com/download/#macos)
or something

2. setup pipenv
```sh
$ pip install pipenv

# .bashrc
eval "$(pipenv --completion)"
```

3. setup heroku command
```sh
$ brew install heroku
$ heroku login
```

## Running Locally

1. download this repository
2. move to downloaded directory
3. add .env
```
HELLO_MESSAGE='hello world! .env file is enabled.'
```

5. run apprication
```sh
$ heroku local
     or
$ pipenv shell
$ python index.py
```
6. access to 'http://localhost:5000'


## Deploy to heroku

```sh
heroku login
heroku create
heroku plugins:install heroku-config
heroku config:push
git push heroku master
```

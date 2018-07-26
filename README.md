# Python Flask Heroku Skeleton

## Install to Mac

1. setup heroku and pyenv command
```sh
$ brew install heroku pyenv
```

```
# .bashrc
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

```sh
$ pyenv install 3.6.4
$ pyenv global 3.6.4
```

2. setup pipenv
```sh
$ pip install pipenv
```

```
# .bashrc
$ eval "$(pipenv --completion)"
```


## Running Locally

1. download this repository
2. move to downloaded directory
3. pipenv install

```sh
$ pipenv install
```

4. add .env
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
git push heroku master
```

# Installation

If you want to install this project on your computer you need to copy this project

```bash
git clone https://github.com/InkSmile/CxDojoTest.git
```
Then you need to install [Docker](https://docs.docker.com/engine/install/)

Run command

```bash
docker build -t foo . && docker run -it foo
```

Wait until docker buil your project. In your browser enter url http://0.0.0.0:8000

Make migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Then you need to create super user using your terminal. 

```bash
python manage.py createsuperuser
```

If you want upload data into db you need sign up as admin and click to `Date Generate`

Then you need to choose a csv file and click `Generate`

If docker does not work you can run it manually

First of all, install poetry

```bash
pip install poetry
```
or use this curl

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Then you need install packages

```bash
poetry install
```

After makemigrations

```bash
python manage.py makemigrations
```

Migrate

```bash
python manage.py migrate
```

And run server

```bash
python manage.py runserver
```
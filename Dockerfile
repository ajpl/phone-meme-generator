FROM tiangolo/meinheld-gunicorn-flask:python3.8

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system --ignore-pipfile

COPY ./app /app

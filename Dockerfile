FROM tiangolo/meinheld-gunicorn-flask:python3.8-alpine3.11

RUN apk add --update-cache \
    zlib-dev \
    jpeg-dev \
    gcc \
    musl-dev \
&& rm -rf /var/cache/apk/* \
&& pip install Pillow==8.0.1 \
&& apk del \
    zlib-dev \
    jpeg-dev \
    gcc \
    musl-dev

RUN pip install -U pip pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system --ignore-pipfile

COPY ./app /app

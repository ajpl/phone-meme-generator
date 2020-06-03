FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN echo "wsgi-disable-file-wrapper = true" >> uwsgi.ini

COPY ./app /app
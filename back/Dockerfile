FROM python:3.6-alpine

COPY ./ /back

WORKDIR /back

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install pipenv && \
    pipenv install && \
    pipenv run python manage.py migrate

CMD ["pipenv", "run", "python", "manage.py", "runserver"]

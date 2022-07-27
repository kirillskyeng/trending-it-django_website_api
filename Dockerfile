FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PORT 8000

EXPOSE $PORT

VOLUME [ "/app/db.sqlite3" ]

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

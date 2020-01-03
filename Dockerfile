FROM tiangolo/uwsgi-nginx-flask

WORKDIR /app

ENV FLASK_APP "lambda/uploadFileToS3.py"
ENV FLASK_DEBUG True

COPY ./app /app

EXPOSE 5000

#CMD export FLASK_APP=uploadFileToS3.py && flask run

CMD flask run --host=13.233.35.143

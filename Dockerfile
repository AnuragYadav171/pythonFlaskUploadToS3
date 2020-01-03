FROM anuragyadav171/flaskapp:flask

WORKDIR /app

ENV FLASK_APP "lambda/uploadFileToS3.py"
ENV FLASK_DEBUG True

COPY ./app /app

EXPOSE 5000

#CMD export FLASK_APP=uploadFileToS3.py && flask run

# CMD flask run --host localhost

CMD ["flask", "run", "--host", "172.17.0.1", "--port", "5000"]

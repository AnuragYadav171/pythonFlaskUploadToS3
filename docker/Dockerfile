FROM abc

WORKDIR /app

ENV FLASK_APP "lambda/uploadFileToS3.py"
ENV FLASK_DEBUG True

COPY ../. /app

EXPOSE 5000

#CMD export FLASK_APP=uploadFileToS3.py && flask run

CMD flask run --host=0.0.0.0

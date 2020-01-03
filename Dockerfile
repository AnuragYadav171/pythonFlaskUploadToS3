FROM abc

WORKDIR /app

ENV FLASK_APP "uploadFileToS3.py"
ENV FLASK_DEBUG True

COPY . /app

EXPOSE 5000

#CMD flask run --host=0.0.0.0

CMD flask run --host `awk 'END{print $1}' /etc/hosts` --port 5000

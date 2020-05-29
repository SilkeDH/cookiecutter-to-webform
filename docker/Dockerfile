FROM python:3.7

COPY . /app

WORKDIR /app/

ENV PYTHONPATH=/app

RUN pip3 install gunicorn && pip install -r /app/requirements.txt

EXPOSE 5001

ENV TIMEOUT 60
ENV ENABLE_HTTPS False
ENV WORKERS 1

COPY ./docker/start.sh /start.sh

CMD ["/bin/bash","/start.sh"]
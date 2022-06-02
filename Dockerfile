FROM python:3.7

RUN mkdir /app
RUN mkdir /app/log
RUN echo >/app/log/log.log
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]

FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip3 install flask 
RUN pip3 install pika

CMD ["nohup","python","message.py",";","python3", "-m", "flask", "run", "--host=0.0.0.0"]

FROM python:3.10

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

EXPOSE 8080

COPY ./ /app

CMD ["python", "main.py"]

FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apk add --no-cache bash

CMD ["bash", "-c", "python server.py" ]

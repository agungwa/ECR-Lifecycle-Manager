FROM python:3.9-slim

RUN pip install boto3

COPY . /app
WORKDIR /app

ENTRYPOINT ["/app/action.sh"]
FROM python:3.9-slim

RUN pip install boto3

COPY . /action
WORKDIR /action

ENTRYPOINT ["python", "/action/action.py"]
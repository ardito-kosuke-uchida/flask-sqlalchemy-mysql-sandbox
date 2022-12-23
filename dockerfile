FROM python:3.10

WORKDIR /work
ADD ./ /work
RUN pip install -e .
